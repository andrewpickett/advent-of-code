package main

import (
	"strconv"
	"utils"
)

var data = getData(utils.GetLines("input.txt"))

func getData(lines []string) []int {
	var data []int
	for _, s := range lines {
		i, _ := strconv.Atoi(s)
		data = append(data, i)
	}
	return data
}

func partOne() string {
	for i := 0; i < len(data)-1; i++ {
		for j := i + 1; j < len(data); j++ {
			if data[i]+data[j] == 2020 {
				return strconv.Itoa(data[i] * data[j])
			}
		}
	}
	return ""
}

func partTwo() string {
	for i := 0; i < len(data)-2; i++ {
		for j := i + 1; j < len(data)-1; j++ {
			for k := j + 1; k < len(data); k++ {
				if data[i]+data[j]+data[k] == 2020 {
					return strconv.Itoa(data[i] * data[j] * data[k])
				}
			}
		}
	}
	return ""
}

func main() {
	utils.RunWithTimer(partOne) // main.partOne -- 197451 -- took 0 ms
	utils.RunWithTimer(partTwo) // main.partTwo -- 138233720 -- took 1 ms
}
