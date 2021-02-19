const puzzle = require('./puzzle')
const data = require('./input')

test('partOne examples', () => {
	expect(puzzle.partOne('abcdef')).toBe(609043);
	expect(puzzle.partOne('pqrstuv')).toBe(1048970);
});

test('partOne', () => {
	const d = puzzle.parseData(data);
	expect(puzzle.partOne(d)).toBe(282749);
});

test('partTwo examples', () => {
});

test('partTwo', () => {
	const d = puzzle.parseData(data);
	expect(puzzle.partTwo(d)).toBe(9962624);
});
