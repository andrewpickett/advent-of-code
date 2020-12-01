package aoc;

public abstract class AocPuzzle<S, T> {
	protected final S input;
	public abstract T partOne();
	public abstract T partTwo();
	public abstract S getInput(String location);

	public AocPuzzle(String inputLocation) {
		input = getInput(inputLocation);
	}

	public void runPartOneWithTimer() {
		long start = System.currentTimeMillis();
		T result = partOne();
		long end = System.currentTimeMillis();
		System.out.printf("partOne -- %s -- took %d ms%n", result, (end - start));
	}

	public void runPartTwoWithTimer() {
		long start = System.currentTimeMillis();
		T result = partTwo();
		long end = System.currentTimeMillis();
		System.out.printf("partTwo -- %s -- took %d ms%n", result, (end - start));
	}

	public void run() {
		System.out.println(partOne());
		System.out.println(partTwo());
	}

	public void runWithTimers() {
		runPartOneWithTimer();
		runPartTwoWithTimer();
	}
}
