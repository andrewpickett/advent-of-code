package main

import (
	"fmt"
	"strconv"
	"utils"
)

func getData(lines []string) []int {
	var data []int
	for _, s := range lines {
		i, _ := strconv.Atoi(s)
		data = append(data, i)
	}
	return data
}

func partOne(data []int) int {
	for i := 0; i < len(data)-1; i++ {
		for j := i + 1; j < len(data); j++ {
			if data[i]+data[j] == 2020 {
				return data[i] * data[j]
			}
		}
	}
	return 0
}

func partTwo(data []int) int {
	for i := 0; i < len(data)-2; i++ {
		for j := i + 1; j < len(data)-1; j++ {
			for k := j + 1; k < len(data); k++ {
				if data[i]+data[j]+data[k] == 2020 {
					return data[i] * data[j] * data[k]
				}
			}
		}
	}
	return 0
}

func main() {
	var data = getData(utils.GetLines("input.txt"))
	fmt.Println(partOne(data))
	fmt.Println(partTwo(data))
}
