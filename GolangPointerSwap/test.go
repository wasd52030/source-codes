package main

import "fmt"

func swap(a *int, b *int) {
	temp := *a
	*a = *b
	*b = temp
}

func main() {
	a := 3
	b := 45
	fmt.Printf("before swap => a=%v b=%v\n", a, b)
	swap(&a, &b)
	fmt.Printf("after swap => a=%v b=%v\n", a, b)
}
