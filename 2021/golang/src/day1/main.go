package main

import (
	"utils"
)

var data = getData(utils.GetLines("input.txt"))

func getData(lines []string) []string {
	return lines
}

func partOne() string {
	return ""
}

func partTwo() string {
	return ""
}

func main() {
	utils.RunWithTimer(partOne) // main.partOne --  -- took 0 ms
	utils.RunWithTimer(partTwo) // main.partTwo --  -- took 0 ms
}
