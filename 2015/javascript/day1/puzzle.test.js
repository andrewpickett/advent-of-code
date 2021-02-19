const puzzle = require('./puzzle')
const data = require('./input')

test('partOne examples', () => {
	expect(puzzle.partOne('(())')).toBe(0);
	expect(puzzle.partOne('()()')).toBe(0);
	expect(puzzle.partOne('(((')).toBe(3);
	expect(puzzle.partOne('(()(()(')).toBe(3);
	expect(puzzle.partOne('))(((((')).toBe(3);
	expect(puzzle.partOne('())')).toBe(-1);
	expect(puzzle.partOne('))(')).toBe(-1);
	expect(puzzle.partOne(')))')).toBe(-3);
	expect(puzzle.partOne(')())())')).toBe(-3);
});

test('partOne', () => {
	const d = puzzle.parseData(data);
	expect(puzzle.partOne(d)).toBe(138);
});

test('partTwo examples', () => {
	expect(puzzle.partTwo(')')).toBe(1);
	expect(puzzle.partTwo('()())')).toBe(5);
});

test('partTwo', () => {
	const d = puzzle.parseData(data);
	expect(puzzle.partTwo(d)).toBe(1771);
});
