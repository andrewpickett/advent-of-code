package aoc.day3;

import aoc.AocPuzzle;
import aoc.utils.NoSolutionFoundException;

import java.util.List;

import static aoc.utils.LineReader.readLinesAsInts;

public class Puzzle extends AocPuzzle<List<Integer>, Integer> {

	public static void main(String[] args) {
		new Puzzle("day3/input.txt").runWithTimers();
	}

	public Puzzle(String inputLocation) {
		super(inputLocation);
	}

	@Override
	public Integer partOne() {
		throw new NoSolutionFoundException();
	}

	@Override
	public Integer partTwo() {
		throw new NoSolutionFoundException();
	}

	@Override
	public List<Integer> getInput(String location) {
		return readLinesAsInts(location);
	}
}
