package aoc.day2;

import aoc.AocPuzzle;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static aoc.utils.LineReader.readLines;

public class Puzzle extends AocPuzzle<List<List<String>>, Integer> {

	public static void main(String[] args) {
		new Puzzle("day2/input.txt").runWithTimers();
	}

	public Puzzle(String inputLocation) {
		super(inputLocation);
	}

	@Override
	public Integer partOne() {
		int dist = 0;
		int depth = 0;
		for (List<String> d : input) {
			switch (d.get(0)) {
				case "forward":
					dist += Integer.parseInt(d.get(1));
					break;
				case "down":
					depth += Integer.parseInt(d.get(1));
					break;
				case "up":
					depth -= Integer.parseInt(d.get(1));
					break;
			}
		}
		return dist * depth;
	}

	@Override
	public Integer partTwo() {
		int dist = 0;
		int depth = 0;
		int aim = 0;
		for (List<String> d : input) {
			switch (d.get(0)) {
				case "forward":
					dist += Integer.parseInt(d.get(1));
					depth += aim * Integer.parseInt(d.get(1));
					break;
				case "down":
					aim += Integer.parseInt(d.get(1));
					break;
				case "up":
					aim -= Integer.parseInt(d.get(1));
					break;
			}
		}
		return dist * depth;
	}


	@Override
	public List<List<String>> getInput(String location) {
		List<String> lines = readLines(location);
		List<List<String>> retVal = new ArrayList<>();
		for (String line : lines) {
			retVal.add(Arrays.asList(line.split(" ")));
		}
		return retVal;
	}
}
