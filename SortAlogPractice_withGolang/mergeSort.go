//reference：https://www.bilibili.com/video/BV1k34y1S71P

package main

func merge[T Number](left []T, right []T) (res []T) {
	i, j := 0, 0 // i->left point;j->right point

	for i < len(left) && j < len(right) {
		//左右兩陣列依序取出元素進行比較，較小的推入result
		if left[i] < right[j] {
			res = append(res, left[i])
			i++
		} else {
			res = append(res, right[j])
			j++
		}
	}

	// 將兩個slice中位於對應的index計數器後面的元素灌進res slice
	res = append(res, left[i:]...)
	res = append(res, right[j:]...)

	return
}

func mergeSort[T Number](arr []T) (res []T) {
	if len(arr) <= 1 {
		return arr
	}

	mid := len(arr) / 2
	left := arr[:mid]
	right := arr[mid:]

	return merge(mergeSort(left), mergeSort(right))
}
