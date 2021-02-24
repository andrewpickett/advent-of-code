let utils = require('../aoc_utils')
let data = require('./input')

function run(part) {
	const d = parseData(data);
	return (part === 1) ? utils.runWithTimer(partOne, d) : utils.runWithTimer(partTwo, d);
}

function parseData(data) {
	let reindeer = {}
	data.trim().split('\n').forEach(s => {
		let parts = s.split(' ');
		reindeer[parts[0]] = {"speed":parseInt(parts[3]), "duration":parseInt(parts[6]), "rest":parseInt(parts[13]), "pos":0, "pts":0};
	});
	return reindeer;
}

function calculateTotalDistance(r, t) {
	let rem = (t % (r['duration'] + r['rest']));
	let remSp = (rem > r['duration'] ? r['duration'] : rem) * r['speed'];
	let fullSp = Math.floor(t / (r['duration'] + r['rest'])) * r['speed'] * r['duration']
	return fullSp + remSp;
}

function updatePositions(data, t) {
	for (const [key, value] of Object.entries(data)) {
		value['pos'] = calculateTotalDistance(value, t);
	}
}

function partOne(data) {
	updatePositions(data, 2503);
	let dists = [];
	for (const [key, value] of Object.entries(data)) {
		dists.push(value['pos']);
	}
	return Math.max(...dists);
}

function partTwo(data) {
	for (let i = 1; i <= 2503; i++) {
		updatePositions(data, i);
		let currMaxVal = 0;
		let currMaxKey = null;
		for (const [key, value] of Object.entries(data)) {
			if (value['pos'] > currMaxVal) {
				currMaxVal = value['pos'];
				currMaxKey = key;
			}
		}
		data[currMaxKey]['pts'] += 1;
	}
	let pts = [];
	for (const [key, value] of Object.entries(data)) {
		pts.push(value['pts']);
	}
	return Math.max(...pts);
}

module.exports = { run, parseData, partOne, partTwo }
