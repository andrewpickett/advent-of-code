package main

import (
	"fmt"
	"utils"
)

func getData(lines []string) []string {
	return lines
}

func partOne(data []string) int {
	for _, e := range data {
		fmt.Println(e)
	}
	return 1119
}

func main() {
	var data = getData(utils.GetLines("input.txt"))
	fmt.Println(partOne(data))
}
