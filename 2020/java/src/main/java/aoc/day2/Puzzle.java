package aoc.day2;

import aoc.AocPuzzle;

import java.util.List;
import java.util.stream.Collectors;

import static aoc.utils.LineReader.readLines;

public class Puzzle extends AocPuzzle<List<Puzzle.InputData>, Integer> {

	public static void main(String[] args) {
		new Puzzle("day2/input.txt").runWithTimers();
	}

	public Puzzle(String inputLocation) {
		super(inputLocation);
	}

	@Override
	public Integer partOne() {
		int numValid = 0;
		for (InputData d : input) {
			long cnt = d.getPassword().chars().filter(c -> c == d.getLetter()).count();
			numValid += (d.getMin() <= cnt && cnt <= d.getMax()) ? 1 : 0;
		}
		return numValid;
	}

	@Override
	public Integer partTwo() {
		int numValid = 0;
		for (InputData d : input) {
			int currCount = 0;
			currCount += (d.getPassword().charAt(d.getMin()-1) == d.getLetter()) ? 1 : 0;
			currCount += (d.getPassword().charAt(d.getMax()-1) == d.getLetter()) ? 1 : 0;
			numValid += (currCount == 1) ? 1 : 0;
		}
		return numValid;
	}

	@Override
	public List<InputData> getInput(String location) {
		return readLines(location).stream().map(InputData::parse).collect(Collectors.toList());
	}

	static class InputData {
		private int min;
		private int max;
		private char letter;
		private String password;

		public int getMin() {
			return min;
		}

		public void setMin(int min) {
			this.min = min;
		}

		public int getMax() {
			return max;
		}

		public void setMax(int max) {
			this.max = max;
		}

		public char getLetter() {
			return letter;
		}

		public void setLetter(char letter) {
			this.letter = letter;
		}

		public String getPassword() {
			return password;
		}

		public void setPassword(String password) {
			this.password = password;
		}

		public static InputData parse(String input) {
			InputData d = new InputData();
			String[] line = input.split(" ");
			d.setMin(Integer.parseInt(line[0].split("-")[0]));
			d.setMax(Integer.parseInt(line[0].split("-")[1]));
			d.setLetter(line[1].substring(0, 1).charAt(0));
			d.setPassword(line[2]);
			return d;
		}
	}
}
