package main

import (
	"database/sql"
	"time"
)

// ActivityScanner scans heartbeats for activities
type ActivityScanner struct {
	DB         *sql.DB
	CompanyID  int
	DeviceID   string
	WindowSize int

	fields []Field
}

const getPivots = `
SELECT    mf.field_name,
          mf.pivot,
          mf.radius
FROM      managementzones m
LEFT JOIN managementzones_fields mf
       ON m.category_id = mf.field_id
WHERE     m.category = 'field'
  AND     mf.boundary_type = 'circle'
  AND     m.company_id = $1`

// getPivots gets all the circular fields for a company
func (as *ActivityScanner) getPivots() error {
	rows, err := as.DB.Query(getPivots, PerryCID)
	if err != nil {
		return err
	}
	defer func() { _ = rows.Close() }() // Best effort.

	for rows.Next() {
		pivot := Pivot{}
		if err := rows.Scan(&pivot.Name, &pivot.Center, &pivot.Radius); err != nil {
			return err
		}
		as.fields = append(as.fields, pivot)
	}
	if err := rows.Err(); err != nil {
		return err
	}
	return nil
}

const getPolygons = `
SELECT    mf.field_name,
          mf.polygon,
FROM      managementzones m
LEFT JOIN managementzones_fields mf
       ON m.category_id = mf.field_id
WHERE     m.category = 'field'
  AND     mf.boundary_type = 'polygon'
  AND     m.company_id = $1`

// getPolygons gets all the polygon fields for a company
func (as *ActivityScanner) getPolygons() error {
	rows, err := as.DB.Query(getPolygons, PerryCID)
	if err != nil {
		return err
	}
	defer func() { _ = rows.Close() }() // Best effort.

	for rows.Next() {
		polygon := Polygon{}
		if err := rows.Scan(&polygon.Name, &polygon.Polygon); err != nil {
			return err
		}
		as.fields = append(as.fields, polygon)
	}
	if err := rows.Err(); err != nil {
		return err
	}
	return nil
}

// getFields fetches all the fields for a company
func (as *ActivityScanner) getFields() error {
	if err := as.getPivots(); err != nil {
		return err
	}
	return as.getPolygons()
}

// Run runs the activity scanner.
func (as *ActivityScanner) Run() error {
	if err := as.getFields(); err != nil {
		return err
	}
	// Query heartbeats
	var (
		now       = time.Now()
		yesterday = now.Add(-24 * time.Hour)
	)
	rows, err := as.DB.Query(getHeartbeats, as.DeviceID, yesterday, now)
	if err != nil {
		return err
	}
	defer func() { _ = rows.Close() }() // Best effort.

	// Scan heartbeats
	var (
		i      = 0
		window = make([]*Heartbeat, WindowSize)
	)
	for rows.Next() {
		// Scan the heartbeat
		hb := &Heartbeat{}
		if err := hb.ScanRow(rows); err != nil {
			return err
		}
		// If
		if i < WindowSize {
			window = append(window, hb)
			continue
		}
	}
	if err := rows.Err(); err != nil {
		return err
	}
	return nil
}
