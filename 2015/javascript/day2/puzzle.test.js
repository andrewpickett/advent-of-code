const puzzle = require('./puzzle')
const data = require('./input')

test('partOne examples', () => {
	expect(puzzle.partOne([[2,3,4]])).toBe(58);
	expect(puzzle.partOne([[1,1,10]])).toBe(43);
});

test('partOne', () => {
	const d = puzzle.parseData(data);
	expect(puzzle.partOne(d)).toBe(1588178);
});

test('partTwo examples', () => {
	expect(puzzle.partTwo([[2,3,4]])).toBe(34);
	expect(puzzle.partTwo([[1,1,10]])).toBe(14);
});

test('partTwo', () => {
	const d = puzzle.parseData(data);
	expect(puzzle.partTwo(d)).toBe(3783758);
});
