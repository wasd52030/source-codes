// reference -> https://www.bilibili.com/video/BV1Te4y1W7Lu/

package main

import (
	"fmt"
	"os"
	"os/exec"
	"time"
)

const (
	c = 10
	r = 10
)

type World [c][r]int

//reference -> https://stackoverflow.com/questions/19209425/how-can-i-clear-the-console-with-golang-in-windows
func cls() {
	command := exec.Command("cmd", "/c", "cls")
	command.Stdout = os.Stdout
	command.Run()
}

func main() {
	var GameWorld World
	GameWorld[0][1] = 1
	GameWorld[1][2] = 1

	GameWorld[2][0] = 1
	GameWorld[2][1] = 1
	GameWorld[2][2] = 1

	GameWorld[6][7] = 1
	GameWorld[7][6] = 1
	GameWorld[7][7] = 1
	GameWorld[7][8] = 1
	GameWorld[8][7] = 1

	var cmd string
	for cmd != "q" {
		cls()
		world := GameWorld
		output := ""
		for i := 0; i < c; i++ {
			for j := 0; j < r; j++ {
				state := 0
				if !(i == 0 || j == 0) {
					state += GameWorld[i-1][j-1]
				}

				if !(i == 0) {
					state += GameWorld[i-1][j]
				}

				if !(i == 0 || j == r-1) {
					state += GameWorld[i-1][j+1]
				}

				if !(j == 0) {
					state += GameWorld[i][j-1]
				}

				if !(j == r-1) {
					state += GameWorld[i][j+1]
				}

				if !(i == c-1 || j == 0) {
					state += GameWorld[i+1][j-1]
				}

				if !(i == c-1) {
					state += GameWorld[i+1][j]
				}

				if !(i == c-1 || j == r-1) {
					state += GameWorld[i+1][j]
				}

				if state < 2 || state > 3 {
					world[i][j] = 0
				} else if state == 3 {
					world[i][j] = 1
				}

				if world[i][j] == 1 {
					//reference -> https://chunchaichang.blogspot.com/2011/07/printf.html
					output += "\033[47m  \033[0m"
				} else {
					output += "  "
				}
			}
			output += "\n"
		}
		fmt.Print(output)
		GameWorld = world
		time.Sleep(500 * time.Millisecond)
	}
}
