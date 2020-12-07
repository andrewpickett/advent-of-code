package aoc.day3;

import aoc.AocPuzzle;
import aoc.utils.NoSolutionFoundException;

import java.util.List;

import static aoc.utils.LineReader.readLines;

public class Puzzle extends AocPuzzle<char[][], Integer> {

	public static void main(String[] args) {
		new Puzzle("day3/input.txt").runWithTimers();
	}

	public Puzzle(String inputLocation) {
		super(inputLocation);
	}

	public Integer calcTreeCount(int rise, int run) {
		Point currPos = new Point();
		int count = 0;
		while (currPos.getY() < input.length) {
			count += input[currPos.getY()][currPos.getX()] == '#' ? 1 : 0;
			currPos.takeStep(rise, run, input[0].length);
		}
		return count;
	}

	@Override
	public Integer partOne() {
		return calcTreeCount(1, 3);
	}

	@Override
	public Integer partTwo() {
		return calcTreeCount(1, 1) * calcTreeCount(1, 3) * calcTreeCount(1, 5) * calcTreeCount(1, 7) * calcTreeCount(2, 1);
	}

	@Override
	public char[][] getInput(String location) {
		List<String> lines = readLines(location);
		char[][] tmp = new char[lines.size()][lines.get(0).length()];
		for (int i = 0; i < lines.size(); i++) {
			tmp[i] = lines.get(i).toCharArray();
		}

		return tmp;
	}

	class Point {
		private int x;
		private int y;

		public Point() {
			this(0, 0);
		}

		public Point(int x, int y) {
			setX(x);
			setY(y);
		}

		public void takeStep(int rise, int run, int max) {
			setX((x + run) % max);
			setY(y + rise);
		}

		public int getX() {
			return x;
		}

		public void setX(int x) {
			this.x = x;
		}

		public int getY() {
			return y;
		}

		public void setY(int y) {
			this.y = y;
		}

		@Override
		public String toString() {
			return "(" + getX() + "," + getY() + ")";
		}
	}
}
