let utils = require('../aoc_utils')
let data = require('./input')

function run(part) {
	const d = parseData(data);
	return (part === 1) ? utils.runWithTimer(partOne, d) : utils.runWithTimer(partTwo, d);
}

function parseData(data) {
	let d = data.trim();
	return d.split('\n');
}

function partOne(data) {
	return data.filter(s => {
		if (s.indexOf('ab') >= 0 || s.indexOf('cd') >= 0 || s.indexOf('pq') >= 0 || s.indexOf('xy') >= 0) {
			return false;
		}
		if ((s.match(/[aeiou]/g) || []).length < 3) {
			return false;
		}
		for (let i = 0; i < s.length - 1; i++) {
			if (s.charAt(i) === s.charAt(i+1)) {
				return true;
			}
		}
		return false;
	}).length;
}

function partTwo(data) {
	return data.filter(s => {
		let valid = false;
		for (let i = 0; i < s.length - 3; i++) {
			let pair = '' + s.charAt(i) + s.charAt(i+1);
			if (s.substr(i+2).indexOf(pair) >= 0) {
				valid = true;
				break;
			}
		}
		if (valid) {
			for (let i = 0; i < s.length - 2; i++) {
				if (s.charAt(i) === s.charAt(i + 2)) {
					return true;
				}
			}
		}
		return false;
	}).length;
}

module.exports = { run, parseData, partOne, partTwo }
