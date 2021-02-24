const puzzle = require('./puzzle')
const data = require('./input')

test('partOne examples', () => {
	expect(puzzle.partOne([0, 1, 2, 3, 4, 5, 6, 7])).toBe('abcdffaa');
	expect(puzzle.partOne([6, 7, 8, 9, 10, 11, 11, 12])).toBe('ghjaabcc');
});

test('partOne', () => {
	const d = puzzle.parseData(data);
	expect(puzzle.partOne(d)).toBe('hepxxyzz');
});

test('partTwo examples', () => {
});

test('partTwo', () => {
	const d = puzzle.parseData(data);
	expect(puzzle.partTwo(d)).toBe('heqaabcc');
});
