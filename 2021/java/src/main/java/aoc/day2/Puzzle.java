package aoc.day2;

import aoc.AocPuzzle;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static aoc.utils.LineReader.readLines;

public class Puzzle extends AocPuzzle<List<Instruction>, Integer> {

	public static void main(String[] args) {
		new Puzzle().runWithTimers();
	}

	public Puzzle() {
		super();
	}

	public Puzzle(List<Instruction> instructions) {
		super(instructions);
	}

	@Override
	public Integer partOne() {
		Position p = new Position();
		for (Instruction d : input) {
			switch (d.direction()) {
				case "forward" -> p.moveForward(d.amount());
				case "down" -> p.moveDown(d.amount());
				case "up" -> p.moveUp(d.amount());
			}
		}
		return p.calculate();
	}

	@Override
	public Integer partTwo() {
		Position p = new Position();
		for (Instruction d : input) {
			switch (d.direction()) {
				case "forward" -> {
					p.moveForward(d.amount());
					p.moveDown(p.getAim() * d.amount());
				}
				case "down" -> p.aimDown(d.amount());
				case "up" -> p.aimUp(d.amount());
			}
		}
		return p.calculate();
	}


	@Override
	public List<Instruction> getInput() {
		List<String> lines = readLines(getInputLocation());
		List<Instruction> retVal = new ArrayList<>();
		for (String line : lines) {
			String[] parts = line.split(" ");
			retVal.add(new Instruction(parts[0], Integer.parseInt(parts[1])));
		}
		return retVal;
	}

	@Override
	public String getInputLocation() {
		return "day2/input.txt";
	}
}

class Position {
	private int horizontal;
	private int depth;
	private int aim;

	public void moveForward(int amount) {
		horizontal += amount;
	}

	public void moveDown(int amount) {
		depth += amount;
	}

	public void moveUp(int amount) {
		depth -= amount;
	}

	public void aimDown(int amount) {
		aim += amount;
	}

	public void aimUp(int amount) {
		aim -= amount;
	}

	public int calculate() {
		return horizontal * depth;
	}

	public int getAim() {
		return aim;
	}
}

record Instruction(String direction, int amount) {
}
