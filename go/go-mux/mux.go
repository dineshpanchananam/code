package main

import (
	"fmt"
	"time"
)

// import (
// 	// 	"fmt"
// 	"github.com/gorilla/mux"
// 	"net/http"
// )

// func Hello(res http.ResponseWriter,
// 	req *http.Request) {
// }

func main() {
	go fmt.Println("hello")
	fmt.Println("world")
	p := make(chan int, 4)
	for i := 0; i < 5; i++ {
		go fmt.Println(i)
	}
	time.Sleep(1 * time.Millisecond)
}

func Hello() {
	return
}
