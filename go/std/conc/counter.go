package main

import "fmt"

var count = 0

func get() int {
	count += 1
	return count
}

func fetch(n int) {
	for i := 0; i < n; i++ {
		get()
	}
}

func main() {
	ch := make(chan int)
	for i := 0; i < 40; i++ {
		go func() {
			fetch(10)
			ch <- 1
		}()
	}
	for i := 0; i < 4; i++ {
		<-ch
	}
	fmt.Println(count)
}
