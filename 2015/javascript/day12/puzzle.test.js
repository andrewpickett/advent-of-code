const puzzle = require('./puzzle')
const data = require('./input')

test('partOne examples', () => {
	expect(puzzle.partOne(puzzle.parseData('[1,2,3]'))).toBe(6);
	expect(puzzle.partOne(puzzle.parseData('{"a":2,"b":4}'))).toBe(6);
	expect(puzzle.partOne(puzzle.parseData('[[[3]]]'))).toBe(3);
	expect(puzzle.partOne(puzzle.parseData('{"a":{"b":4},"c":-1}'))).toBe(3);
	expect(puzzle.partOne(puzzle.parseData('{"a":[-1,1]}'))).toBe(0);
	expect(puzzle.partOne(puzzle.parseData('[-1,{"a":1}]'))).toBe(0);
	expect(puzzle.partOne(puzzle.parseData('[]'))).toBe(0);
	expect(puzzle.partOne(puzzle.parseData('{}'))).toBe(0);
});

test('partOne', () => {
	const d = puzzle.parseData(data);
	expect(puzzle.partOne(d)).toBe(119433);
});

test('partTwo examples', () => {
	expect(puzzle.partTwo(puzzle.parseData('[1,2,3]'))).toBe(6);
	expect(puzzle.partTwo(puzzle.parseData('[1,{"c":"red","b":2},3]'))).toBe(4);
	expect(puzzle.partTwo(puzzle.parseData('{"d":"red","e":[1,2,3,4],"f":5}'))).toBe(0);
	expect(puzzle.partTwo(puzzle.parseData('[1,"red",5]'))).toBe(6);
});

test('partTwo', () => {
	const d = puzzle.parseData(data);
	expect(puzzle.partTwo(d)).toBe(68466);
});
