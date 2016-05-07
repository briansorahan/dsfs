package main

import (
	"database/sql"
	"time"
)

// Beacon represents a kontakt beacon
type Beacon struct {
	ID    string `json:"proximity_uuid"`
	Major int    `json:"major"`
	Minor int    `json:"minor"`
}

// HeartbeatBeacon represents a beacon's information as part of a heartbeat.
type HeartbeatBeacon struct {
	Beacon
	Distance float64 `json:"distance"`
	Paired   bool    `json:"is_paired"`
}

// Heartbeat is a packet of data sent from a device in a tractor.
type Heartbeat struct {
	Point

	ID               int               `json:"id,omitempty"`
	CompanyID        int               `json:"company_id"`
	UserID           string            `json:"user_id"`
	ManagementzoneID string            `json:"managementzone_id"`
	DeviceID         string            `json:"device_id"`
	Heading          float64           `json:"heading"`
	Speed            float64           `json:"speed"`
	Timestamp        int64             `json:"timestamp"`
	CreatorID        string            `json:"creator_id"`
	CreatedAt        time.Time         `json:"created_at"`
	Beacons          []HeartbeatBeacon `json:"beacons"`
}

// ScanRow scans a heartbeat from a database row.
func (heartbeat *Heartbeat) ScanRow(rows *sql.Rows) error {
	return rows.Scan(
		&heartbeat.ID,
		&heartbeat.UserID,
		&heartbeat.DeviceID,
		&heartbeat.Longitude,
		&heartbeat.Latitude,
		&heartbeat.Heading,
		&heartbeat.Speed,
		&heartbeat.Timestamp,
		&heartbeat.CreatedAt,
		&heartbeat.ManagementzoneID,
		&heartbeat.CreatorID,
	)
}

// getHeartbeats is the query for getting heartbeats.
// The heartbeats must belong to a single company and be scoped
// to a time range.
const getHeartbeats = `
SELECT heartbeat_id,
       user_id,
       device_id,
       longitude,
       latitude,
       heading,
       speed,
       hb_time,
       created_at,
       managementzone_id,
       creator_id
FROM   heartbeats
WHERE  device_id  =  $1
  AND  created_at >= $2
  AND  created_at <  $3`

// getHeartbeatBeacons is the query for getting the beacons associated
// with a heartbeat
const getHeartbeatBeacons = `
SELECT hb.beacon_proximity_uuid,
       hb.major,
       hb.minor,
       hb.distance,
       hb.is_paired
FROM   heartbeats_beacons hb
WHERE  heartbeats_beacons.heartbeat_id = $1`
