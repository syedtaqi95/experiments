package main

import (
	"fmt"
	"log"
	"net/http"
)

const port = 8081

func main() {

	fmt.Println("Starting HTTP server on port", port)

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "Hello, you've requested: %s\n", r.URL.Path)
	})

	log.Fatal(http.ListenAndServe(fmt.Sprintf(":%d", port), nil))
}
