package main

import (
	"aoc2021utils"
	"fmt"
)

func getData(lines []string) []string {
	return lines
}

func partOne(data []string) int {
	return 1119
}

func main() {
	var data = getData(aoc2021utils.GetLines("2021/golang/src/day1/input.txt"))
	fmt.Println(partOne(data))
}
