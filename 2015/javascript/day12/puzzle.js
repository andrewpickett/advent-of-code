let utils = require('../aoc_utils')
let data = require('./input')

function run(part) {
	const d = parseData(data);
	return (part === 1) ? utils.runWithTimer(partOne, d) : utils.runWithTimer(partTwo, d);
}

function parseData(data) {
	return JSON.parse(data);
}

function partOne(data) {
	let tmp = JSON.stringify(data).split(/[\[\],:{}[a-zA-Z'"\\]/).filter(s => s.length > 0);
	return (tmp.length > 0) ? parseInt(tmp.reduce((a, b) => parseInt(a) + parseInt(b))) : 0;
}

function findReds(data) {
	let elemsToRemoveObj = [];
	let elemsToRemoveArr = [];
	if (Array.isArray(data)) {
		for (let i = 0; i < data.length; i++) {
			if (typeof data[i] === 'object') {
				if (findReds(data[i])) {
					elemsToRemoveArr.push(data[i]);
				}
			}
		}
	} else if (typeof data === 'object') {
		for (const [key, value] of Object.entries(data)) {
			if (typeof value === 'object') {
				if (findReds(data[key])) {
					elemsToRemoveObj.push(key);
				}
			}
			if (value === 'red') {
				return true;
			}
		}
	}

	elemsToRemoveObj.forEach(e => delete data[e]);
	elemsToRemoveArr.forEach(e => data.splice(data.indexOf(e), 1));
	return false;
}

function partTwo(data) {
	if (findReds(data)) {
		return 0;
	}

	let tmp = JSON.stringify(data).split(/[\[\],:{}[a-zA-Z'"\\]/).filter(s => s.length > 0);
	return (tmp.length > 0) ? parseInt(tmp.reduce((a, b) => parseInt(a) + parseInt(b))) : 0;
}

module.exports = { run, parseData, partOne, partTwo }
