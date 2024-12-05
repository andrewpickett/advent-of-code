package utils

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"reflect"
	"runtime"
	"strconv"
	"strings"
	"time"
)

type fn func(d interface{}) string

func GetLines(f string) []string {
	if f == "" {
		f = "input.txt"
	}
	file, err := os.Open(f)
	if err != nil {
		log.Fatal(err)
	}
	defer func(file *os.File) {
		err := file.Close()
		if err != nil {
			return
		}
	}(file)

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines
}

func GetIntsFromLine(line string, delim string) []int {
	var nums []int
	if delim == "" {
		delim = " "
	}
	for _, strNum := range strings.Split(line, delim) {
		num, err := strconv.Atoi(strNum)
		if err != nil {
			continue
		}
		nums = append(nums, num)
	}
	return nums
}

func RunWithTimer(track fn, d interface{}) {
	start := time.Now()
	result := track(d)
	fmt.Println(fmt.Sprintf("%s -- %s -- took %d ms", runtime.FuncForPC(reflect.ValueOf(track).Pointer()).Name(), result, time.Since(start)/1000000))
}

func GetDataWithTimer(track fn, filename string) {
	start := time.Now()
	result := track(filename)
	fmt.Println(fmt.Sprintf("%s -- %s -- took %d ms", runtime.FuncForPC(reflect.ValueOf(track).Pointer()).Name(), result, time.Since(start)/1000000))
}
