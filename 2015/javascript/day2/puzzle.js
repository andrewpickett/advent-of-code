let utils = require('../aoc_utils')
let data = require('./input')

function run(part) {
	const d = parseData(data);
	return (part === 1) ? utils.runWithTimer(partOne, d) : utils.runWithTimer(partTwo, d);
}

function parseData(data) {
	let d = [];
	let lines = data.trim().split('\n');
	for (let i = 0; i < lines.length; i++) {
		let dimInts = [];
		let dims = lines[i].split('x');
		for (let j = 0; j < dims.length; j++) {
			dimInts.push(parseInt(dims[j]));
		}
		d.push(dimInts);
	}
	return d;
}

function partOne(data) {
	let total = 0;
	for (let i = 0; i < data.length; i++) {
		total += 2*data[i][0]*data[i][1] + 2*data[i][1]*data[i][2] + 2*data[i][2]*data[i][0] + (data[i].reduce((a,b) => a*b) / Math.max(...data[i]));
	}
	return total;
}

function partTwo(data) {
	let total = 0;
	for (let i = 0; i < data.length; i++) {
		total += 2*((data[i].reduce((a,b) => a+b) - Math.max(...data[i]))) + data[i].reduce((a,b,) => a*b)
	}
	return total;
}

module.exports = { run, parseData, partOne, partTwo }
