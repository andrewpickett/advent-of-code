const puzzle = require('./puzzle')
const data = require('./input')

test('partOne examples', () => {
	expect(puzzle.partOne([199,200,208,210,200,207,240,269,260,263])).toBe(7);
});

test('partOne', () => {
	const d = puzzle.parseData(data);
	expect(puzzle.partOne(d)).toBe(1766);
});

test('partTwo examples', () => {
	expect(puzzle.partTwo([199,200,208,210,200,207,240,269,260,263])).toBe(5);
});

test('partTwo', () => {
	const d = puzzle.parseData(data);
	expect(puzzle.partTwo(d)).toBe(1797);
});
