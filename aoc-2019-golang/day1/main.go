package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func getLines(f string) []string {
	file, err := os.Open(f)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines
}

func main() {
	var lines = getLines("aoc-2019-golang/day1/input.txt")
	fmt.Println(lines)
	fmt.Println(len(lines))
}
