package main

import (
	"aoc2019utils"
	"fmt"
	"strconv"
)

func calcMass(val int) int {
	return val / 3 - 2
}

func calcTotal(start int) int {
	if start <= 0 {
		return 0
	}
	return start + calcTotal(calcMass(start))
}

func partOne(lines []string) int {
	var total = 0
	for _, element := range lines {
		var newVal, _ = strconv.Atoi(element)
		total += calcMass(newVal)
	}
	return total
}

func partTwo(lines []string) int {
	var total = 0
	for _, element := range lines {
		var newVal, _ = strconv.Atoi(element)
		total += calcTotal(calcMass(newVal))
	}
	return total
}

func main() {
	var lines = aoc2019utils.GetLines("day1/input.txt")
	fmt.Println(partOne(lines))
	fmt.Println(partTwo(lines))
}
