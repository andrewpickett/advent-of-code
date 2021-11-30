package main

import (
	"math"
	"strconv"
	"strings"
	"utils"
)

var data = getData(utils.GetLines("input.txt"))

func contains(s [][]int, i []int) bool {
	for _, v := range s {
		if v[0] == i[0] && v[1] == i[1] {
			return true
		}
	}

	return false
}

func moveCurPos(curPos []int, curDir *int, dir string) {
	if string(dir[0]) == "L" {
		*curDir = (*curDir - 1) % 4
	} else {
		*curDir = (*curDir + 1) % 4
	}
	idx, _ := strconv.Atoi(dir[1:])
	if *curDir == 2 || *curDir == 3 || *curDir == -1 || *curDir == -2 {
		idx *= -1
	}
	curIdx := 0
	if *curDir%2 == 0 {
		curIdx = 1
	}
	curPos[curIdx] += idx
}

func getDistance(pos []int) int {
	return int(math.Abs(float64(pos[0]))) + int(math.Abs(float64(pos[1])))
}

func getData(lines []string) []string {
	return strings.Split(strings.ReplaceAll(lines[0], " ", ""), ",")
}

func partOne() string {
	curPos := make([]int, 2)
	curDir := 0 // 0=N, 1=E, 2=S, 3=W
	for _, dir := range data {
		moveCurPos(curPos, &curDir, dir)
	}
	return strconv.Itoa(getDistance(curPos))
}

func partTwo() string {
	visitedPos := make([][]int, 0)
	curPos := make([]int, 2)
	visitedPos = append(visitedPos, []int{0, 0})
	curDir := 0 // 0=N, 1=E, 2=S, 3=W
	for _, dir := range data {
		oldPos := []int{curPos[0], curPos[1]}
		moveCurPos(curPos, &curDir, dir)
		if curPos[0] == oldPos[0] {
			if curPos[1] > oldPos[1] {
				for i := oldPos[1] + 1; i <= curPos[1]; i++ {
					tmpPos := []int{curPos[0], i}
					if contains(visitedPos, tmpPos) {
						return strconv.Itoa(getDistance(tmpPos))
					}
					visitedPos = append(visitedPos, tmpPos)
				}
			} else {
				for i := oldPos[1] - 1; i >= curPos[1]; i-- {
					tmpPos := []int{curPos[0], i}
					if contains(visitedPos, tmpPos) {
						return strconv.Itoa(getDistance(tmpPos))
					}
					visitedPos = append(visitedPos, tmpPos)
				}
			}
		} else {
			if curPos[0] > oldPos[0] {
				for i := oldPos[0] + 1; i <= curPos[0]; i++ {
					tmpPos := []int{i, curPos[1]}
					if contains(visitedPos, tmpPos) {
						return strconv.Itoa(getDistance(tmpPos))
					}
					visitedPos = append(visitedPos, tmpPos)
				}
			} else {
				for i := oldPos[0] - 1; i >= curPos[0]; i-- {
					tmpPos := []int{i, curPos[1]}
					if contains(visitedPos, tmpPos) {
						return strconv.Itoa(getDistance(tmpPos))
					}
					visitedPos = append(visitedPos, tmpPos)
				}
			}
		}
	}
	return ""
}

func main() {
	utils.RunWithTimer(partOne) // main.partOne -- 239 -- took 0 ms
	utils.RunWithTimer(partTwo) // main.partTwo -- 141 -- took 1 ms
}
