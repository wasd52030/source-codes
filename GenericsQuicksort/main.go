package main

import (
	"fmt"
	"math/rand"
	"time"
)

type Number interface {
	int | int16 | int32 | int64 | float32 | float64
}

func quickSort[T Number](arr []T) (res []T) {
	if len(arr) < 2 {
		return arr
	}

	key := arr[0]
	var left []T
	var right []T

	for _, item := range arr[1:] {
		if item <= key {
			left = append(left, item)
		} else {
			right = append(right, item)
		}
	}
	res = append(res, quickSort(left)...)
	res = append(res, key)
	res = append(res, quickSort(right)...)

	return
}

func main() {
	rand.Seed(time.Now().Unix())
	var u []int
	var v []float32
	for i := 0; i < 10; i++ {
		u = append(u, rand.Intn(100))
	}
	for i := 0; i < 10; i++ {
		v = append(v, rand.Float32()*100)
	}

	fmt.Printf("before sort: %+v\n", u)
	fmt.Printf("after sort: %+v\n", quickSort(u))

	fmt.Printf("before sort: %+v\n", v)
	fmt.Printf("after sort: %+v\n", quickSort(v))
}
