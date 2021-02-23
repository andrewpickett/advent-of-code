const puzzle = require('./puzzle')
const data = require('./input')

test('partOne examples', () => {
	expect(puzzle.partOne({
		"London": {"Dublin": 464, "Belfast": 518},
		"Dublin": {"London": 464, "Belfast": 141},
		"Belfast": {"Dublin": 141, "London": 518}
	})).toBe(605);
});

test('partOne', () => {
	const d = puzzle.parseData(data);
	expect(puzzle.partOne(d)).toBe(251);
});

test('partTwo examples', () => {
	expect(puzzle.partTwo({
		"London": {"Dublin": 464, "Belfast": 518},
		"Dublin": {"London": 464, "Belfast": 141},
		"Belfast": {"Dublin": 141, "London": 518}
	})).toBe(982);
});

test('partTwo', () => {
	const d = puzzle.parseData(data);
	expect(puzzle.partTwo(d)).toBe(898);
});
