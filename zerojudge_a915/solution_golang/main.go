package main

import "fmt"

type point struct {
	x, y int
}

func findminpoint(arr []point) (index int) {
	min := arr[0]
	index = 0
	for i := 0; i < len(arr); i++ {
		if arr[i].x < min.x {
			min = arr[i]
			index = i
		} else if arr[i].x == min.x {
			if arr[i].y < min.y {
				min = arr[i]
				index = i
			}
		}
	}
	return
}

func selectsort(arr []point) (result []point) {
	Orisize := len(arr)
	result = make([]point, Orisize)
	for i := 0; i < Orisize; i++ {
		minIndex := findminpoint(arr)
		result[i] = arr[minIndex]
		arr = append(arr[:minIndex], arr[minIndex+1:]...)
	}
	return
}

func main() {
	var d int
	for {
		_, err := fmt.Scanln(&d)
		if err != nil {
			break
		}

		ps := make([]point, d)
		for i := 0; i < d; i++ {
			fmt.Scanf("%v %v\n", &ps[i].x, &ps[i].y)
		}

		for _, i := range selectsort(ps) {
			fmt.Printf("%v %v\n", i.x, i.y)
		}
	}
}
