package main

import (
	"aoc2019utils"
	"fmt"
	"strconv"
)

func partOne(lines []string) int {
	var frequency = 0
	for _, element := range lines {
		var newVal, _ = strconv.Atoi(element)
		frequency += newVal
	}
	return frequency
}

func main() {
	var lines = aoc2019utils.GetLines("day1/input.txt")
	fmt.Println(partOne(lines))
}
