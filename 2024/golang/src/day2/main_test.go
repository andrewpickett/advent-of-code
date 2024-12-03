package main

import (
	"testing"
)

func TestPartOne(t *testing.T) {
	data := GetData("sample.txt")
	want := "2"
	p1 := PartOne(data)
	if want != p1 {
		t.Fatalf(`PartOne = %q, want match for %#q, nil`, p1, want)
	}
}

func TestPartTwo(t *testing.T) {
	data := GetData("sample.txt")
	want := "4"
	p1 := PartTwo(data)
	if want != p1 {
		t.Fatalf(`PartTwo = %q, want match for %#q, nil`, p1, want)
	}
}
