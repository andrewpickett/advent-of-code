package aoc.year2019.day1;

import java.util.List;

import static aoc.year2019.utils.LineReader.readLinesAsInts;

public class AocMain {

	public static void main(String[] args) {
		List<Integer> lines = readLinesAsInts("day1/input.txt");
		System.out.println(partOne(lines)); // 3382284
		System.out.println(partTwo(lines)); // 5070541
	}

	public static int partOne(List<Integer> lines) {
		return lines.stream().mapToInt(i -> calcMass(i)).sum();
	}

	public static int partTwo(List<Integer> lines) {
		return lines.stream().mapToInt(i -> calcTotal(calcMass(i))).sum();
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
