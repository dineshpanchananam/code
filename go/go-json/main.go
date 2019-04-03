package main

import (
	"encoding/json"
	// 	"fmt"
	"log"
)

type regReq struct {
	Username string `json:"username"`
	Password string `json:"secret"`
	Info     map[string]string
}

func main() {
	e := regReq{Username: "dinesh", Password: "1234"}
	e.Info = map[string]string{}
	e.Info["age"] = "25"
	f := map[string]regReq{}
	f["user"] = e
	msg, err := json.MarshalIndent(f, "", "  ")
	if err != nil {
		log.Fatal(err)
	} else {
		log.Println(string(msg))
		d := map[string]regReq{}
		err = json.Unmarshal(msg, &d)
		if err == nil {
			log.Println(d)
		} else {
			log.Println(err)
		}
	}
}
