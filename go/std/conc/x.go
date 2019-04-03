package main

import (
	"fmt"
	"sync"
	"time"
)

func say(s string, m time.Duration) {
	for i := 0; i < 5; i++ {
		time.Sleep(m)
		fmt.Println(s)
	}
}

func main() {
	var wg sync.WaitGroup
	wg.Add(1)
	go func() {
		say("world", 900*time.Millisecond)
		wg.Done()
	}()
	say("hello", 100*time.Millisecond)
	wg.Wait()
}
