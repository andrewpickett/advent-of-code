package aoc.day3;

import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class PuzzleTest {
	private Puzzle puzzle;
	private static final List<Diagnostic> EXAMPLE_INPUT_1 = Arrays.asList(
		new Diagnostic("00100"), new Diagnostic("11110"), new Diagnostic("10110"), new Diagnostic("10111"),
		new Diagnostic("10101"), new Diagnostic("01111"), new Diagnostic("00111"), new Diagnostic("11100"),
		new Diagnostic("10000"), new Diagnostic("11001"), new Diagnostic("00010"), new Diagnostic("01010"));

	@Test
	public void testPart1Example() {
		puzzle = new Puzzle(EXAMPLE_INPUT_1);
		assertEquals(198, puzzle.partOne());
	}

	@Test
	public void testPart1() {
		puzzle = new Puzzle();
		assertEquals(2595824, puzzle.partOne());
	}

	@Test
	public void testPart2Example() {
		puzzle = new Puzzle(EXAMPLE_INPUT_1);
		assertEquals(230, puzzle.partTwo());
	}

	@Test
	public void testPart2() {
		puzzle = new Puzzle();
		assertEquals(2135254, puzzle.partTwo());
	}
}
