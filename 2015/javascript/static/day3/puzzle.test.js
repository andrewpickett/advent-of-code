const puzzle = require('./puzzle')
const data = require('./input')

test('partOne examples', () => {
	expect(puzzle.partOne('>')).toBe(2);
	expect(puzzle.partOne('^>v<')).toBe(4);
	expect(puzzle.partOne('^v^v^v^v^v')).toBe(2);
});

test('partOne', () => {
	const d = puzzle.parseData(data);
	expect(puzzle.partOne(d)).toBe(2565);
});

test('partTwo examples', () => {
	expect(puzzle.partTwo('^v')).toBe(3);
	expect(puzzle.partTwo('^>v<')).toBe(3);
	expect(puzzle.partTwo('^v^v^v^v^v')).toBe(11);
});

test('partTwo', () => {
	const d = puzzle.parseData(data);
	expect(puzzle.partTwo(d)).toBe(2639);
});
