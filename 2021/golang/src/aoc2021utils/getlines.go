package aoc2021utils

import (
	"bufio"
	"log"
	"os"
	"path/filepath"
)

func GetLines(f string) []string {
	abs, _ := filepath.Abs(f)
	file, err := os.Open(abs)
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
