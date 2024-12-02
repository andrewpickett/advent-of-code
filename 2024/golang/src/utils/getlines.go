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

func RunWithTimer(track fn, d interface{}) {
	start := time.Now()
	result := track(d)
	fmt.Println(fmt.Sprintf("%s -- %s -- took %d ms", runtime.FuncForPC(reflect.ValueOf(track).Pointer()).Name(), result, time.Since(start)/1000000))
}

func GetDataWithTimer() {

}

//
//def get_data_with_timer(f, filename):
//stime = time.time_ns()
//result = f(filename)
//etime = time.time_ns()
//print("{} -- took {} ms".format(f.__name__, (etime - stime) // 1000000))
//return result
//
//
//def run_with_timer(f, d):
//stime = time.time_ns()
//result = f(d)
//etime = time.time_ns()
//print("{} -- {} -- took {} ms".format(f.__name__, result, (etime - stime) // 1000000))
//return result
