const puzzle = require('./puzzle')
const data = require('./input')

test('parseData', () => {
	expect(puzzle.parseData('turn on 0,0 through 999,999')).toStrictEqual([{"action": 1, "startX": 0, "startY": 0, "endX": 999, "endY": 999}]);
	expect(puzzle.parseData('toggle 0,0 through 999,0')).toStrictEqual([{"action": 2, "startX": 0, "startY": 0, "endX": 999, "endY": 0}]);
	expect(puzzle.parseData('turn off 499,499 through 500,500')).toStrictEqual([{"action": 0, "startX": 499, "startY": 499, "endX": 500, "endY": 500}]);
});

test('partOne examples', () => {
	expect(puzzle.partOne([{"action": 1, "startX": 0, "startY": 0, "endX": 999, "endY": 999}])).toBe(1000000);
	expect(puzzle.partOne([{"action": 2, "startX": 0, "startY": 0, "endX": 999, "endY": 0}])).toBe(1000);
	expect(puzzle.partOne([{"action": 0, "startX": 499, "startY": 499, "endX": 500, "endY": 500}])).toBe(0);
});

test('partOne', () => {
	const d = puzzle.parseData(data);
	expect(puzzle.partOne(d)).toBe(400410);
});

test('partTwo examples', () => {
	expect(puzzle.partTwo([{"action": 1, "startX": 0, "startY": 0, "endX": 0, "endY": 0}])).toBe(1);
	expect(puzzle.partTwo([{"action": 2, "startX": 0, "startY": 0, "endX": 999, "endY": 999}])).toBe(2000000);
});

test('partTwo', () => {
	const d = puzzle.parseData(data);
	expect(puzzle.partTwo(d)).toBe(15343601);
});
