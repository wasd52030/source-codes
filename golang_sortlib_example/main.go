//以zerojudge_a915這道題為範例
package main

import (
	"fmt"
	"sort"
)

type point struct {
	x, y int
}

type Points []point

func (p Points) Len() int {
	return len(p)
}

func (p Points) Swap(i, j int) {
	p[i], p[j] = p[j], p[i]
}

func (p Points) Less(i, j int) bool {
	if p[i].x == p[j].x {
		return p[i].y < p[j].y
	}
	return p[i].x < p[j].x
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

		sort.Sort(Points(ps))

		for _, i := range ps {
			fmt.Printf("%d %d\n", i.x, i.y)
		}
	}
}
