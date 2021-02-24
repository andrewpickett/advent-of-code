let utils = require('../aoc_utils')
let data = require('./input')

const ALPHA = 'abcdefghijklmnopqrstuvwxyz';

function run(part) {
	const d = parseData(data);
	return (part === 1) ? utils.runWithTimer(partOne, d) : utils.runWithTimer(partTwo, d);
}

function checkRuleOne(d) {
	for (let i = 0; i < d.length - 2; i++) {
		if (d[i] === d[i+1] - 1 && d[i+1] === d[i+2] - 1) {
			return true;
		}
	}
	return false;
}

function checkRuleTwo(d) {
	if (d.indexOf(ALPHA.indexOf('i')) >= 0) {
		return d.indexOf(ALPHA.indexOf('i'));
	} else if (d.indexOf(ALPHA.indexOf('o')) >= 0) {
		return d.indexOf(ALPHA.indexOf('o'));
	} else if (d.indexOf(ALPHA.indexOf('l')) >= 0) {
		return d.indexOf(ALPHA.indexOf('l'));
	}
	return -1;
}

function checkRuleThree(d) {
	let cnt = 0;
	for (let i = 0; i < d.length - 1; i++) {
		if (d[i] === d[i+1]) {
			i += 1;
			cnt += 1;
		}
	}
	return cnt >= 2;
}

function parseData(data) {
	let d = [];
	for (let i = 0; i < data.trim().length; i++) {
		d.push(ALPHA.indexOf(data.trim().charAt(i)));
	}
	return d;
}

function increment(d, pos) {
	d[pos] += 1;
	for (let i = pos; i >= 0; i--) {
		if (d[i] >= 26) {
			d[i] %= 26;
			d[i-1] += 1;
		}
	}
}

function getStrFromData(data) {
	let retVal = '';
	data.forEach(i => retVal += ALPHA.charAt(i));
	return retVal;
}

function getNextPassword(data) {
	while (true) {
		if (!checkRuleOne(data)) {
			increment(data, data.length - 1);
			continue;
		}
		let check = checkRuleTwo(data);
		if (check >= 0) {
			increment(data, check);
			for (let i = check + 1; i < data.length; i++) {
				data[i] = 0;
			}
			continue;
		}
		if (!checkRuleThree(data)) {
			increment(data, data.length - 1);
			continue;
		}
		return getStrFromData(data);
	}
}

function partOne(data) {
	return getNextPassword(data);
}

function partTwo(data) {
	data = parseData(partOne(data));
	increment(data, data.length - 1);
	return getNextPassword(data);
}

module.exports = { run, parseData, partOne, partTwo }
