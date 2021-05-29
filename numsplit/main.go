package main

import "fmt"

func numsplit(i int64) (narr []int64) {
	var d []int64 //原始數據(逆序)

	for i > 10 {
		d = append(d, i%10)
		i /= 10
		if i < 10 {
			d = append(d, i)
		}
	}

	//將原始數據反轉
	for i := len(d) - 1; i > -1; i-- {
		narr = append(narr, d[i])
	}

	return
}

func main() {
	var a int64 = 12345678
	o := numsplit(a)
	fmt.Printf("%v\n", o)
}
