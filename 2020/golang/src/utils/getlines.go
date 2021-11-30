package utils

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"reflect"
	"runtime"
	"time"
)

type fn func() string

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

func RunWithTimer(track fn) {
	start := time.Now()
	result := track()
	fmt.Println(fmt.Sprintf("%s -- %s -- took %d ms", runtime.FuncForPC(reflect.ValueOf(track).Pointer()).Name(), result, time.Since(start)/1000000))
}
