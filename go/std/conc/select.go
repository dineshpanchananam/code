package main

import (
	"fmt"
	"sync"
)

var wg sync.WaitGroup

func sum_arr(i int, j int, c chan int) {
	sum := 0
	for k := i; k < j; k++ {
		sum += k
	}
	c <- sum
	wg.Done()
}

func sum2(n int) (s int) {
	s = 0
	for k := 0; k < n; k++ {
		s += k
	}
	return
}

func sum1(n int) (s int) {
	wg.Add(4)
	c := make(chan int, 4)
	go sum_arr(0, n/4, c)
	go sum_arr(n/4, n/2, c)
	go sum_arr(n/2, 3*n/4, c)
	go sum_arr(3*n/4, n, c)
	wg.Wait()
	close(c)
	s = 0
	for x := range c {
		s += x
	}
	return
}

func main() {
	fmt.Println(sum1(3e9))
	fmt.Println(sum2(3e9))
}
