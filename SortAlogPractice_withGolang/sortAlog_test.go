package main

import (
	"math/rand"
	"testing"
	"time"
)

func Test_mergeSort(t *testing.T) {

	var u []int
	rand.Seed(time.Now().Unix())
	for i := 0; i < 10; i++ {
		u = append(u, rand.Intn(100)+1)
	}

	t.Log(mergeSort(u))
}

func Test_quickSort(t *testing.T) {

	var u []int
	rand.Seed(time.Now().Unix())
	for i := 0; i < 10; i++ {
		u = append(u, rand.Intn(100)+1)
	}

	t.Log(quickSort(u))
}
