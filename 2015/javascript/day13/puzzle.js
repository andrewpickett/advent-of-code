let utils = require('../aoc_utils')
let data = require('./input')

function run(part) {
	const d = parseData(data);
	return (part === 1) ? utils.runWithTimer(partOne, d) : utils.runWithTimer(partTwo, d);
}

function parseData(data) {
	let d = {};
	data.trim().split('\n').forEach(s => {
		let parts = s.substring(0, s.length - 1).split(' ');
		if (!(parts[0] in d)) {
			d[parts[0]] = {};
		}
		d[parts[0]][parts[10]] = parseInt(parts[3]) * (parts[2] === 'gain' ? 1 : -1);
	});
	return d;
}

function getMaxHappiness(data, names) {
	let namePerms = utils.permutator(Array.from(names));
	let currMax = 0;
	for (let i = 0; i < namePerms.length; i++) {
		let currTot = 0;
		for (let j = 0; j < namePerms[i].length; j++) {
			currTot += data[namePerms[i][j]][namePerms[i][(j+1) % namePerms[i].length]];
			currTot += data[namePerms[i][(j+1) % namePerms[i].length]][namePerms[i][j]];
		}
		if (currTot > currMax) {
			currMax = currTot;
		}
	}
	return currMax;
}

function partOne(data) {
	let names = new Set();
	for (const [key, value] of Object.entries(data)) {
		names.add(key);
	}
	return getMaxHappiness(data, names);
}

function partTwo(data) {
	let names = new Set();
	for (const [key, value] of Object.entries(data)) {
		data[key]['Self'] = 0;
		names.add(key);
	}
	data['Self'] = {};
	for (const value of names) {
		data['Self'][value] = 0
	}
	names.add('Self');
	return getMaxHappiness(data, names);
}

module.exports = { run, parseData, partOne, partTwo }
