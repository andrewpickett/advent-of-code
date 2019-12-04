package main.java.day1;

import java.util.List;

import static utils.LineReader.readLinesAsInts;

public class AocMain {

	public static void main(String[] args) {
		List<Integer> lines = readLinesAsInts("day1/input.txt");
		System.out.println(partOne(lines));
		System.out.println(partTwo(lines));
	}

	public static int partOne(List<Integer> lines) {

		int frequency = 0;
		for (Integer line : lines) {
			frequency += line;
		}
		return frequency;
	}

	public static int partTwo(List<Integer> lines) {
		return 0;
	}
}
