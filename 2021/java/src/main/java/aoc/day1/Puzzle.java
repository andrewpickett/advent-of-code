package aoc.day1;

import aoc.AocPuzzle;
import aoc.utils.NoSolutionFoundException;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

import static aoc.utils.LineReader.readLinesAsInts;

public class Puzzle extends AocPuzzle<List<Measurement>, Integer> {

	public static void main(String[] args) {
		new Puzzle().runWithTimers();
	}

	public Puzzle() {
		super();
	}

	public Puzzle(List<Measurement> input) {
		super(input);
	}

	@Override
	public Integer partOne() {
		int count = 0;
		for (int i = 1; i < input.size(); i++) {
			if (input.get(i).value() > input.get(i - 1).value()) {
				count++;
			}
		}
		return count;
	}

	@Override
	public Integer partTwo() {
		int count = 0;
		for (int i = 3; i < input.size(); i++) {
			if (input.get(i).value() + input.get(i - 1).value() + input.get(i - 2).value() > input.get(i - 1).value() + input.get(i - 2).value() + input.get(i - 3).value()) {
				count++;
			}
		}
		return count;
	}

	@Override
	public List<Measurement> getInput() {
		return readLinesAsInts(getInputLocation()).stream().map(item -> new Measurement(item)).toList();
	}

	@Override
	public String getInputLocation() {
		return "day1/input.txt";
	}
}

record Measurement(int value) {
}
