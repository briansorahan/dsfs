package main

import (
	"database/sql"
	"log"
	"sync"
	"time"

	_ "github.com/lib/pq"
)

// PerryCID is the company ID of bill perry
const PerryCID = 2019

// PerryDevices is the list of devices deployed to bill perry's farm
var PerryDevices = []string{
	"cf616c1e-ae87-4b40-af85-8a31f2dae852",
	"3eb3a32b-0d0b-43a4-a8b4-0924489a1324",
	"a717fa28-d8d4-435f-871c-eac5d84f0046",
	"aaea7f26-4702-4d21-b41d-9f0b3adaf6b8",
	"aa2a60c6-2871-4a79-a0e7-9c03fa6017c8",
}

// WindowSize is the number of heartbeats we use to determine the
// size of the moving window.
const WindowSize = 100

func main() {
	// Connect to the database
	db, err := sql.Open("postgres", "sslmode=disable user=leaf dbname=leaf")
	if err != nil {
		log.Fatal(err)
	}
	wg := sync.WaitGroup{}
	for _, deviceID := range PerryDevices {
		wg.Add(1)
		go func(deviceID string) {
			activity := &ActivityScanner{
				DB:         db,
				DeviceID:   deviceID,
				WindowSize: WindowSize,
			}
			start := time.Now()
			if err := activity.Run(); err != nil {
				wg.Done()
				log.Printf("error for device %s: %s\n", deviceID, err)
				return
			}
			// TODO: generate report
			log.Printf("scanner for device %s took %s\n", deviceID, time.Now().Sub(start))
			wg.Done()
		}(deviceID)
	}
	wg.Wait()
}
