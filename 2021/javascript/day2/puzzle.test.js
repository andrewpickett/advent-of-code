const puzzle = require('./puzzle')
const data = require('./input')

test('partOne examples', () => {
	expect(puzzle.partOne([['forward', '5'], ['down', '5'], ['forward', '8'], ['up', '3'], ['down', '8'], ['forward', '2']])).toBe(150);
});

test('partOne', () => {
	const d = puzzle.parseData(data);
	expect(puzzle.partOne(d)).toBe(1660158);
});

test('partTwo examples', () => {
	expect(puzzle.partTwo([['forward', '5'], ['down', '5'], ['forward', '8'], ['up', '3'], ['down', '8'], ['forward', '2']])).toBe(900);
});

test('partTwo', () => {
	const d = puzzle.parseData(data);
	expect(puzzle.partTwo(d)).toBe(1604592846);
});
