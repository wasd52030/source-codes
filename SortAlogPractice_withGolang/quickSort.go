//reference：https://www.bilibili.com/video/BV1Xe4y1Z7hw

package main

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
