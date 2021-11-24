const puzzle = require('./puzzle')
const data = require('./input')

test('partOne examples', () => {
	expect(puzzle.partOne('')).toBe(0);
});

test('partOne', () => {
	const d = puzzle.parseData(data);
	expect(puzzle.partOne(d)).toBe(0);
});

test('partTwo examples', () => {
	expect(puzzle.partTwo('')).toBe(0);
});

test('partTwo', () => {
	const d = puzzle.parseData(data);
	expect(puzzle.partTwo(d)).toBe(0);
});
