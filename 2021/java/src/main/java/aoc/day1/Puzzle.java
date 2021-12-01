package aoc.day1;

import aoc.AocPuzzle;
import aoc.utils.NoSolutionFoundException;

import java.util.List;

import static aoc.utils.LineReader.readLinesAsInts;

public class Puzzle extends AocPuzzle<List<Integer>, Integer> {

	public static void main(String[] args) {
		new Puzzle("day1/input.txt").runWithTimers();
	}

	public Puzzle(String inputLocation) {
		super(inputLocation);
	}

	@Override
	public Integer partOne() {
		int count = 0;
		for (int i = 1; i < input.size(); i++) {
			if (input.get(i) > input.get(i - 1)) {
				count++;
			}
		}
		return count;
	}

	@Override
	public Integer partTwo() {
		int count = 0;
		for (int i = 3; i < input.size(); i++) {
			if (input.get(i) + input.get(i - 1) + input.get(i - 2) > input.get(i - 1) + input.get(i - 2) + input.get(i - 3)) {
				count++;
			}
		}
		return count;
	}

	@Override
	public List<Integer> getInput(String location) {
		return readLinesAsInts(location);
	}
}
