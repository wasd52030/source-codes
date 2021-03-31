package main

import (
	"fmt"
)

type matrix_size struct {
	m int64 //column
	n int64 //row
}

func matrix_init(k matrix_size) [][]int64 {
	var a [][]int64
	var x int64
	for j := 0; j < int(k.m); j++ {
		var n []int64
		for i := 0; i < int(k.n); i++ {
			fmt.Printf("輸入矩陣元素A(%d,%d)為: ", j+1, i+1)
			fmt.Scanf("%d\n", &x)
			n = append(n, x)
		}
		a = append(a, n)
	}
	return a
}

func matrix_muit(a [][]int64, b [][]int64) [][]int64 {
	var result [][]int64
	if len(a[0:][0]) != len(b) {
		fmt.Println("無法相乘")
	} else {
		for i := 0; i < len(a); i++ {
			var n []int64
			for j := 0; j < len(b[0:][0]); j++ {
				var x int64
				var y int64
				for k := 0; k < len(b); k++ {
					x = a[i][k] * b[k][j]
					y += x
				}
				n = append(n, y)
			}
			result = append(result, n)
		}
	}
	return result
}

func main() {
	a := matrix_size{}
	fmt.Print("第一個矩陣的大小m*m(m、n之間請用空格隔開)=")
	fmt.Scanf("%d %d\n", &a.m, &a.n)
	A := matrix_init(a)

	b := matrix_size{}
	fmt.Print("第一個矩陣的大小m*m(m、n之間請用空格隔開)=")
	fmt.Scanf("%d %d\n", &b.m, &b.n)
	B := matrix_init(b)

	O := matrix_muit(A, B)
	for i := 0; i < len(O); i++ {
		for j := 0; j < len(O[0:]); j++ {
			fmt.Printf("%d ", O[i][j])
		}
		fmt.Println()
	}
}
