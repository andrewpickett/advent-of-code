const puzzle = require('./puzzle')
const data = require('./input')

test('partOne examples', () => {
	expect(puzzle.runStep('1')).toBe('11');
	expect(puzzle.runStep('11')).toBe('21');
	expect(puzzle.runStep('21')).toBe('1211');
	expect(puzzle.runStep('1211')).toBe('111221');
	expect(puzzle.runStep('111221')).toBe('312211');
});

test('partOne', () => {
	const d = puzzle.parseData(data);
	expect(puzzle.partOne(d)).toBe(492982);
});

test('partTwo examples', () => {
});

test('partTwo', () => {
	const d = puzzle.parseData(data);
	expect(puzzle.partTwo(d)).toBe(6989950);
});
