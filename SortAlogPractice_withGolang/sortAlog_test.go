package main

import (
	"math/rand"
	"testing"
	"time"
)

func TestSort(t *testing.T) {

	var u []int
	rand.Seed(time.Now().Unix())
	for i := 0; i < 10; i++ {
		u = append(u, rand.Intn(100)+1)
	}

	t.Log(mergeSort(u))
}
