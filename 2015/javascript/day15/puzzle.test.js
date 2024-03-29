const puzzle = require('./puzzle')
const data = require('./input')

test('partOne examples', () => {
});

test('partOne', () => {
	const d = puzzle.parseData(data);
	expect(puzzle.partOne(d)).toBe(222870);
});

test('partTwo examples', () => {
});

test('partTwo', () => {
	const d = puzzle.parseData(data);
	expect(puzzle.partTwo(d)).toBe(117936);
});
