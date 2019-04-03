package main

import "fmt"

// List type
type List struct {
	data int
	next *List
}

func main() {
	l := &List{1, &List{2, &List{3, nil}}}
	for curr := l; curr != nil; curr = curr.next {
		fmt.Println(curr.data)
	}
}
