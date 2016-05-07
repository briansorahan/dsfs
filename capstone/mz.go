package main

import (
	geo "github.com/kellydunn/golang-geo"
	paulgeo "github.com/paulmach/go.geo"
)

// Point is a geospatial point
type Point struct {
	Latitude  float64 `json:"lat"`
	Longitude float64 `json:"long"`
}

func (p *Point) Scan(src interface{}) error {
	return nil
}

// Field provides the method set for all fields
type Field interface {
	Contains(p Point) bool
}

// Polygon defines a field that is shaped like a polygon
type Polygon struct {
	*geo.Polygon

	Name string
}

// Contains returns true if the polygon contains the heartbeat
func (polygon Polygon) Contains(p Point) bool {
	return false
}

// Pivotis a field shaped like a circle
type Pivot struct {
	Center Point   `json:"center"`
	Radius float64 `json:"radius"`
	Name   string  `json:"name"`
}

// Contains returns true if the pivot contains the heartbeat
func (pivot Pivot) Contains(p Point) bool {
	return false
}
