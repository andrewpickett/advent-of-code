package aoc.day3;

import aoc.AocPuzzle;

import java.util.List;

import static aoc.utils.LineReader.readLines;

public class Puzzle extends AocPuzzle<List<Diagnostic>, Integer> {

	public static void main(String[] args) {
		new Puzzle().runWithTimers();
	}

	public Puzzle() {
		super();
	}

	public Puzzle(List<Diagnostic> instructions) {
		super(instructions);
	}

	@Override
	public Integer partOne() {
		Diagnostic gammaRate = new Diagnostic("");
		Diagnostic epsilonRate = new Diagnostic("");
		for (int i = 0; i < input.get(0).getValue().length(); i++) {
			int num_ones = 0;
			for (Diagnostic d : input) {
				num_ones += d.getBitValue(i);
			}
			gammaRate.append((num_ones >= input.size() / 2) ? "1" : "0");
			epsilonRate.append((num_ones >= input.size() / 2) ? "0" : "1");
		}
		return gammaRate.getIntValue() * epsilonRate.getIntValue();
	}

	public Diagnostic calculateRating(boolean oRating) {
		Diagnostic filterVal = new Diagnostic("");
		for (int i = 0; i < input.get(0).getValue().length(); i++) {
			List<Diagnostic> rems = input.stream().filter(e -> e.getValue().startsWith(filterVal.getValue())).toList();
			if (rems.size() == 1) {
				return rems.get(0);
			}
			int numValues = 0;
			for (Diagnostic d : rems) {
				numValues += (oRating && d.getBitValue(i) == 1) || (!oRating && d.getBitValue(i) == 0) ? 1 : 0;
			}
			filterVal.append((numValues > rems.size() / 2.0 || (oRating && numValues == rems.size() / 2.0)) ? "1" : "0");
		}
		return filterVal;
	}

	@Override
	public Integer partTwo() {
		return calculateRating(true).getIntValue() * calculateRating(false).getIntValue();
	}


	@Override
	public List<Diagnostic> getInput() {
		return readLines(getInputLocation()).stream().map(i -> new Diagnostic(i)).toList();
	}

	@Override
	public String getInputLocation() {
		return "day3/input.txt";
	}
}

class Diagnostic {
	private String value;

	public Diagnostic(String value) {
		this.value = value;
	}

	public String getValue() {
		return value;
	}

	public void append(String bit) {
		value += bit;
	}

	public int getBitValue(int index) {
		return Integer.parseInt(value.substring(index, index + 1));
	}

	public int getIntValue() {
		return Integer.parseInt(value, 2);
	}

	public String toString() {
		return value;
	}
}
