package aoc.year2018.day1;

import static aoc.year2018.utils.LineReader.readLines;

import java.util.List;

public class AocMain {

	public static void main(String[] args) {
		List<String> lines = readLines("day1/input.txt");
		System.out.println(partOne(lines));
	}

	public static int partOne(List<String> lines) {
		int frequency = 0;
		for (String line : lines) {
			frequency += Integer.parseInt(line);
		}
		return frequency;
	}
}
