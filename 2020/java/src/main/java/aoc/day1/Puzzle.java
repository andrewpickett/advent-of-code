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
		for (int i = 0; i < input.size(); i++) {
			int first = input.get(i);
			for (int j = i + 1; j < input.size(); j++) {
				int second = input.get(j);
				if (first + second == 2020) {
					return first * second;
				}
			}
		}
		throw new NoSolutionFoundException();
	}

	@Override
	public Integer partTwo() {
		for (int i = 0; i < input.size(); i++) {
			int first = input.get(i);
			for (int j = i + 1; j < input.size(); j++) {
				int second = input.get(j);
				for (int k = j + 1; k < input.size(); k++) {
					int third = input.get(k);
					if (first + second + third == 2020) {
						return first * second * third;
					}
				}
			}
		}
		throw new NoSolutionFoundException();
	}

	@Override
	public List<Integer> getInput(String location) {
		return readLinesAsInts(location);
	}
}
