package main

import "fmt"

type tree struct {
	data  int
	left  *tree
	right *tree
}

func (t *tree) InOrder() {
	if t.left != nil {
		t.left.InOrder()
	}
	fmt.Println(t.data)
	if t.right != nil {
		t.right.InOrder()
	}
}

func main() {
	r := &tree{1, nil, nil}
	f := &tree{3, nil, nil}
	g := &tree{2, r, f}
	g.InOrder()
}
