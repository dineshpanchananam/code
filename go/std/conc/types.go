package main

import "sync"
import "fmt"

var wg sync.WaitGroup

func main() {
	wg.Add(100)
	for i := 0; i < 100; i++ {
		go func(k int) {
			wg.Done()
		}(i)
	}
	wg.Wait()
	const A = 3
	const B = 2e20 / A

	fmt.Println("7.0/3.0 = ", 7.0+3.0)
	fmt.Println(B)
	fmt.Println(1 + 3)
	fmt.Println(d(3e10, 1))
	d := []int{}
	d = append(d, 3)
	d = append(d, 1)
	d = append(d, 2)
	fmt.Println(d)
	f := map[string]rune{}
	f["a"] = 'a'
	f["b"] = 'b'
	f["c"] = 'c'
	f["d"] = rune("d"[0])
	fmt.Println(f)
	for key, _ := range f {
		fmt.Print(key, " ")
	}
	fmt.Println()

	i := 0
	for i < 12 {
		fmt.Print(i, " ")
		i++
	}
	fmt.Println()
	fmt.Printf("%T\n", i)

	var p [3][3]int
	for i := 3; i > 0; i-- {
		for j := 3; j > 0; j-- {
			p[i-1][j-1] = i * j
		}
	}
	fmt.Println(p)
	for _, row := range p {
		fmt.Println(row[0:2:3])
	}

}

func d(a int64, b int64) int64 {
	return a + b
}

// func main() {
// 	threads := 4
// 	// 	wg.Add(threads)
// 	c := make(chan int)
// 	for k := 0; k < threads; k++ {
// 		go func(x chan int) {
// 			s := 0
// 			for i := 0; i < 10000; i++ {
// 				s += i
// 			}
// 			x <- s
// 			// 	wg.Done()
// 		}(c)
// 	}
// 	// 	wg.Wait()
// 	s := 0
// 	// 	close(c)
// 	for k := 0; k < threads; k++ {
// 		s += <-c
// 	}
// 	fmt.Println(s)
// }
