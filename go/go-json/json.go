package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

type Person struct {
	Name     string `json:"name"`
	Age      int    `json:"age"`
	Location string `json:"loc"`
}

func main() {
	m := Person{}
	m.Name = "Dinesh"
	m.Age = 25
	m.Location = "NYC"
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		bytes, _ := json.Marshal(m)
		fmt.Fprintf(w, string(bytes))
	})
	http.ListenAndServe(":8080", nil)
}
