package main

import (
	"math"
	"slices"
	"strconv"
	"utils"
)

func GetData(filename string) interface{} {
	lines := utils.GetLines(filename)
	var nums [][]int
	for _, line := range lines {
		nums = append(nums, utils.GetIntsFromLine(line, " "))
	}
	return nums
}

func PartOne(d interface{}) string {
	data := d.([][]int)
	s := 0
	for _, x := range data {
		if TrySafetyCheck(x) {
			s += 1
		}
	}
	return strconv.Itoa(s)
}

func PartTwo(d interface{}) string {
	data := d.([][]int)
	s := 0
	for _, x := range data {
		if TrySafetyCheck(x) {
			s += 1
		} else {
			for i := 0; i < len(x); i++ {
				copied := make([]int, len(x))
				copy(copied, x)
				if TrySafetyCheck(append(copied[:i], copied[i+1:]...)) {
					s += 1
					break
				}
			}
		}
	}
	return strconv.Itoa(s)
}

func TrySafetyCheck(x []int) bool {
	reversed := make([]int, len(x))
	copy(reversed, x)
	slices.Reverse(reversed)
	if slices.IsSorted(x) || slices.IsSorted(reversed) {
		for i := 0; i < len(x)-1; i++ {
			if math.Abs(float64(x[i]-x[i+1])) <= 0 || math.Abs(float64(x[i]-x[i+1])) >= 4 {
				return false
			}
		}
	} else {
		return false
	}
	return true
}

func main() {
	data := GetData("input.txt")
	utils.RunWithTimer(PartOne, data)
	utils.RunWithTimer(PartTwo, data)
}
