package main

import "fmt"

// Context a
type Context struct {
	a int
	b chan int
	c float32
	d float64
	e bool
	f map[string]rune
}

func main() {
	a := make(chan int, 0)
	go func() { a <- 3 }()
	go func() { a <- 4 }()
	fmt.Println(<-a)
	fmt.Println(<-a)
}
