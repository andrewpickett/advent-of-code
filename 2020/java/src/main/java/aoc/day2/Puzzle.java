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
		return (int) input.stream().filter(InputData::isValidPartOnePassword).count();
	}

	@Override
	public Integer partTwo() {
		return (int) input.stream().filter(InputData::isValidPartTwoPassword).count();
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

		private InputData(int min, int max, char letter, String password) {
			setMin(min);
			setMax(max);
			setLetter(letter);
			setPassword(password);
		}

		public int getLetterCount() {
			return (int) getPassword().chars().filter(c -> c == getLetter()).count();
		}

		public boolean isValidPartOnePassword() {
			int count = getLetterCount();
			return getMin() <= count && count <= getMax();
		}

		public boolean isValidPartTwoPassword() {
			return (getPassword().charAt(getMin()-1) == getLetter()) ^ (getPassword().charAt(getMax()-1) == getLetter());
		}

		public static InputData parse(String input) {
			String[] line = input.split(" ");
			return new InputData(Integer.parseInt(line[0].split("-")[0]), Integer.parseInt(line[0].split("-")[1]), line[1].substring(0, 1).charAt(0), line[2]);
		}

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
	}
}
