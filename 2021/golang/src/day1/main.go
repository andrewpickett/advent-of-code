package main

import (
	"strconv"
	"utils"
)

var data = getData(utils.GetLines("input.txt"))

func getData(lines []string) []int {
	var retVal []int
	for _, e := range lines {
		i, _ := strconv.Atoi(e)
		retVal = append(retVal, i)
	}
	return retVal
}

func partOne() string {
	count := 0
	for i := 1; i < len(data); i++ {
		if data[i] > data[i-1] {
			count += 1
		}
	}

	return strconv.Itoa(count)
}

func partTwo() string {
	count := 0
	for i := 3; i < len(data); i++ {
		if data[i]+data[i-1]+data[i-2] > data[i-1]+data[i-2]+data[i-3] {
			count += 1
		}
	}

	return strconv.Itoa(count)
}

func main() {
	utils.RunWithTimer(partOne) // 1766 -- took 0 ms
	utils.RunWithTimer(partTwo) // 1797 -- took 0 ms
}
