package main

import (
	"fmt"
	"runtime"
	"sync"
	"time"
)

var wg sync.WaitGroup

func main() {
	n := 100
	wg.Add(n)
	fmt.Println(runtime.NumCPU())
	for i := 0; i < n; i++ {
		go func() {
			time.Sleep(time.Second)
			wg.Done()
		}()
	}
	fmt.Println(runtime.NumGoroutine())
	wg.Wait()
}
