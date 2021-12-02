package main

import (
	"strconv"
	"strings"
	"utils"
)

var data = getData(utils.GetLines("input.txt"))

func getData(lines []string) [][]string {
	var retVal [][]string
	for _, e := range lines {
		retVal = append(retVal, strings.Split(e, " "))
	}
	return retVal
}

func partOne() string {
	dist := 0
	depth := 0
	for _, d := range data {
		i, _ := strconv.Atoi(d[1])
		if d[0] == "forward" {
			dist += i
		} else if d[0] == "down" {
			depth += i
		} else if d[0] == "up" {
			depth -= i
		}
	}

	return strconv.Itoa(depth * dist)
}

func partTwo() string {
	dist := 0
	depth := 0
	aim := 0
	for _, d := range data {
		i, _ := strconv.Atoi(d[1])
		if d[0] == "forward" {
			dist += i
			depth += aim * i
		} else if d[0] == "down" {
			aim += i
		} else if d[0] == "up" {
			aim -= i
		}
	}

	return strconv.Itoa(depth * dist)
}

func main() {
	utils.RunWithTimer(partOne) // 1660158 -- took 0 ms
	utils.RunWithTimer(partTwo) // 1604592846 -- took 0 ms
}
