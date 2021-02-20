const puzzle = require('./puzzle')
const data = require('./input')

test('partOne examples', () => {
	expect(puzzle.partOne(['123 -> a', '456 -> y', 'a AND y -> d', 'a OR y -> e', 'a LSHIFT 2 -> f', 'y RSHIFT 2 -> g', 'NOT a -> h', 'NOT y -> i'])).toBe(123);
	expect(puzzle.partOne(['123 -> x', '456 -> a', 'x AND a -> d', 'x OR a -> e', 'x LSHIFT 2 -> f', 'a RSHIFT 2 -> g', 'NOT x -> h', 'NOT a -> i'])).toBe(456);
	expect(puzzle.partOne(['123 -> x', '456 -> y', 'x AND y -> a', 'x OR y -> e', 'x LSHIFT 2 -> f', 'y RSHIFT 2 -> g', 'NOT x -> h', 'NOT y -> i'])).toBe(72);
	expect(puzzle.partOne(['123 -> x', '456 -> y', 'x AND y -> d', 'x OR y -> a', 'x LSHIFT 2 -> f', 'y RSHIFT 2 -> g', 'NOT x -> h', 'NOT y -> i'])).toBe(507);
	expect(puzzle.partOne(['123 -> x', '456 -> y', 'x AND y -> d', 'x OR y -> e', 'x LSHIFT 2 -> a', 'y RSHIFT 2 -> g', 'NOT x -> h', 'NOT y -> i'])).toBe(492);
	expect(puzzle.partOne(['123 -> x', '456 -> y', 'x AND y -> d', 'x OR y -> e', 'x LSHIFT 2 -> f', 'y RSHIFT 2 -> a', 'NOT x -> h', 'NOT y -> i'])).toBe(114);
	expect(puzzle.partOne(['123 -> x', '456 -> y', 'x AND y -> d', 'x OR y -> e', 'x LSHIFT 2 -> f', 'y RSHIFT 2 -> g', 'NOT x -> a', 'NOT y -> i'])).toBe(65412);
	expect(puzzle.partOne(['123 -> x', '456 -> y', 'x AND y -> d', 'x OR y -> e', 'x LSHIFT 2 -> f', 'y RSHIFT 2 -> g', 'NOT x -> h', 'NOT y -> a'])).toBe(65079);
});

test('partOne', () => {
	const d = puzzle.parseData(data);
	expect(puzzle.partOne(d)).toBe(16076);
});

test('partTwo examples', () => {
});

test('partTwo', () => {
	const d = puzzle.parseData(data);
	expect(puzzle.partTwo(d)).toBe(2797);
});
