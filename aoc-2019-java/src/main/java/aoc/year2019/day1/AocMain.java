package aoc.year2019.day1;

import java.util.List;

import static aoc.year2019.utils.LineReader.readLines;
import static java.lang.Integer.parseInt;

public class AocMain {

	public static void main(String[] args) {
		List<String> lines = readLines("day1/input.txt");
		System.out.println(partOne(lines));
		System.out.println(partTwo(lines));
	}

	public static int partOne(List<String> lines) {
		int total = 0;
		for (String line : lines) {
			total += calcMass(parseInt(line));
		}
		return total;
	}

	public static int partTwo(List<String> lines) {
		int total = 0;
		for (String line : lines) {
			total += calcTotal(calcMass(parseInt(line)));
		}
		return total;
	}

	private static int calcMass(int start) {
		// Don't need to "floor" since we know it's an int dividing an int...it will automatically truncate decimals.
		return (start / 3) - 2;
	}

	private static int calcTotal(int start) {
		if (start <= 0) {
			return 0;
		}
		return start + calcTotal(calcMass(start));
	}
}
