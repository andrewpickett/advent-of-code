package main

import (
	"math"
	"sort"
	"strconv"
	"strings"
	"utils"
)

func GetData(filename string) interface{} {
	lines := utils.GetLines(filename)
	var l1 []int
	var l2 []int
	for _, line := range lines {
		parts := strings.Split(line, "   ")
		atoi, _ := strconv.Atoi(parts[0])
		l1 = append(l1, atoi)

		atoi, _ = strconv.Atoi(parts[1])
		l2 = append(l2, atoi)
	}
	sort.Slice(l1, func(i, j int) bool {
		return l1[i] < l1[j]
	})
	sort.Slice(l2, func(i, j int) bool {
		return l2[i] < l2[j]
	})
	return [][]int{l1, l2}
}

func PartOne(d interface{}) string {
	data := d.([][]int)

	s := 0
	for i, num := range data[0] {
		s += int(math.Abs(float64(num - data[1][i])))
	}
	return strconv.Itoa(s)
}

func PartTwo(d interface{}) string {
	data := d.([][]int)

	counts := make(map[int]int)
	for _, num := range data[1] {
		counts[num]++
	}

	s := 0
	for _, num := range data[0] {
		s += num * counts[num]
	}
	return strconv.Itoa(s)
}

func main() {
	data := GetData("input.txt")
	utils.RunWithTimer(PartOne, data)
	utils.RunWithTimer(PartTwo, data)
}
