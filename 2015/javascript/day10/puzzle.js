let utils = require('../aoc_utils')
let data = require('./input')

function run(part) {
	const d = parseData(data);
	return (part === 1) ? utils.runWithTimer(partOne, d) : utils.runWithTimer(partTwo, d);
}

function parseData(data) {
	return data.trim();
}

function runStep(s) {
	let last_char = s.charAt(0);
	let next_str = '';
	let last_cnt = 1;
	for (let i = 1; i < s.length; i++) {
		if (s.charAt(i) !== last_char) {
			for (let j = 0; j < last_cnt; j++) {
				next_str += last_cnt + last_char;
				last_cnt = 0;
			}
		}
		last_char = s.charAt(i);
		last_cnt += 1;
	}
	next_str += last_cnt + last_char;
	return next_str;
}

function runSteps(s, iters) {
	for (let i = 0; i < iters; i++) {
		s = runStep(s);
	}
	return s.length;
}

function partOne(data) {
	return runSteps(data, 40);
}

function partTwo(data) {
	return runSteps(data, 50);
}

module.exports = { run, runStep, parseData, partOne, partTwo }
