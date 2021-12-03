package aoc.day2;

import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class PuzzleTest {
	private Puzzle puzzle;
	private static final List<Instruction> EXAMPLE_INPUT_1 = Arrays.asList(
		new Instruction("forward", 5),
		new Instruction("down", 5),
		new Instruction("forward", 8),
		new Instruction("up", 3),
		new Instruction("down", 8),
		new Instruction("forward", 2));

	@Test
	public void testPart1Example() {
		puzzle = new Puzzle(EXAMPLE_INPUT_1);
		assertEquals(150, puzzle.partOne());
	}

	@Test
	public void testPart1() {
		puzzle = new Puzzle();
		assertEquals(1660158, puzzle.partOne());
	}

	@Test
	public void testPart2Example() {
		puzzle = new Puzzle(EXAMPLE_INPUT_1);
		assertEquals(900, puzzle.partTwo());
	}

	@Test
	public void testPart2() {
		puzzle = new Puzzle();
		assertEquals(1604592846, puzzle.partTwo());
	}
}
