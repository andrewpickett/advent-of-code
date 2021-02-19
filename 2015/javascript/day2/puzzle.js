let utils = require('../aoc_utils')
let data = require('./input')

function run(part) {
	const d = parseData(data);
	return (part === 1) ? utils.runWithTimer(partOne, d) : utils.runWithTimer(partTwo, d);
}

function parseData(data) {
	let d = [];
	data.trim().split('\n').forEach(line => {
		let dimInts = [];
		line.split('x').forEach(dim => {
			dimInts.push(parseInt(dim));
		});
		d.push(dimInts);
	});
	return d;
}

function partOne(data) {
	let total = 0;
	data.forEach(e => {
		total += 2*e[0]*e[1] + 2*e[1]*e[2] + 2*e[2]*e[0] + (e.reduce((a,b) => a*b) / Math.max(...e));
	})
	return total;
}

function partTwo(data) {
	let total = 0;
	data.forEach(e => {
		total += 2*((e.reduce((a,b) => a+b) - Math.max(...e))) + e.reduce((a,b,) => a*b)
	})
	return total;
}

module.exports = { run, parseData, partOne, partTwo }
