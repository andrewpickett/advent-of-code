const puzzle = require('./puzzle')
const fs = require('fs')

test('partOne examples', () => {
	let d = puzzle.parseData(String.raw`
	""
	"abc"
	"aaa\"aaa"
	"\x27"
	`);
	expect(puzzle.partOne(d)).toBe(12);
});

test('partOne', () => {
	const d = puzzle.parseData(fs.readFileSync(__dirname + "/input.txt", 'utf8'));
	expect(puzzle.partOne(d)).toBe(1350);
});

test('partTwo examples', () => {
	let d = puzzle.parseData(String.raw`
	""
	"abc"
	"aaa\"aaa"
	"\x27"
	`);
	expect(puzzle.partTwo(d)).toBe(19);
});

test('partTwo', () => {
	const d = puzzle.parseData(fs.readFileSync(__dirname + "/input.txt", 'utf8'));
	expect(puzzle.partTwo(d)).toBe(2085);
});
