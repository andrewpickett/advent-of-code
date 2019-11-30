package aoc2019utils

import (
	"bufio"
	"log"
	"os"
)

func GetLines(f string) []string {
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
