let utils = require('../aoc_utils')
let fs = require('fs')

function run(part) {
	const d = parseData(fs.readFileSync(__dirname + "/input.txt'", 'utf8'));
	return (part === 1) ? utils.runWithTimer(partOne, d) : utils.runWithTimer(partTwo, d);
}

/*
 * Because of the fact that we have to ignore escape characters, I had to change how I read in the file. I can't juse
 * use it as a JS file. It's a pain, but it ended up working.
 */
function parseData(data) {
	let f = data.trim().split('\n');
	let tmp = [];
	for (let i of f) {
		tmp.push(i.trim());
	}
	return tmp;
}

function partOne(data) {
	let removedSize = 0;
	data.forEach(d => {
		removedSize += 2;																// Surrounding quotes.
		removedSize += (d.match(/[\\]["]/g) || []).length;					// "\"" becomes """ in memory
		removedSize -= (d.match(/[\\][\\][\\]["]/g) || []).length;		// "\\\"" becomes "\"" in memory
		removedSize += (d.match(/[\\][\\]/g) || []).length;				// "\\" becomes "\" in memory
		removedSize += 3*(d.match(/[\\][x]/g) || []).length;				// "\x##" becomes a single character
		removedSize -= 3*(d.match(/[[\\][\\][x]/g) || []).length;		// ...but "\\x##" only removes the double slash.
		removedSize += 2*(d.match(/[\\][\\][\\][x]/g) || []).length;	// ...but "\\\x##" would become a single character again with a leading slash (accounted for above).
	});
	return removedSize;
}

function partTwo(data) {
	let removedSize = 0;
	data.forEach(d => {
		removedSize += (d.match(/["]/g) || []).length + (d.match(/[\\]/g) || []).length + 2;
	});
	return removedSize;
}

module.exports = { run, parseData, partOne, partTwo }
