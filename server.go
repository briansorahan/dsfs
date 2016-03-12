package main

import (
	"log"
	"net/http"
)

func main() {
	http.Handle("/", http.FileServer(http.Dir(".")))

	if err := http.ListenAndServe(":45678", nil); err != nil {
		log.Fatal(err)
	}
}
