package aoc.day1;

import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class PuzzleTest {
	private Puzzle puzzle;
	private static final List<Measurement> EXAMPLE_INPUT_1 = Arrays.asList(
		new Measurement(199),
		new Measurement(200),
		new Measurement(208),
		new Measurement(210),
		new Measurement(200),
		new Measurement(207),
		new Measurement(240),
		new Measurement(269),
		new Measurement(260),
		new Measurement(263));

	@Test
	public void testPart1Example() {
		puzzle = new Puzzle(EXAMPLE_INPUT_1);
		assertEquals(7, puzzle.partOne());
	}

	@Test
	public void testPart1() {
		puzzle = new Puzzle();
		assertEquals(1766, puzzle.partOne());
	}

	@Test
	public void testPart2Example() {
		puzzle = new Puzzle(EXAMPLE_INPUT_1);
		assertEquals(5, puzzle.partTwo());
	}

	@Test
	public void testPart2() {
		puzzle = new Puzzle();
		assertEquals(1797, puzzle.partTwo());
	}
}
