let utils = require('../aoc_utils')
let data = require('./input')

function run(part) {
	const d = parseData(data);
	return (part === 1) ? utils.runWithTimer(partOne, d) : utils.runWithTimer(partTwo, d);
}

function parseData(data) {
	let d = []
	data.trim().split('\n').forEach(l => {
		let newL = l.substring(l.indexOf("turn") === 0 ? 5 : 0);
		let action = newL.substring(0, newL.indexOf(' '));
		newL = newL.substring(newL.indexOf(' ') + 1);
		let coords = newL.split(' through ');
		let start = coords[0].split(',');
		let end = coords[1].split(',');
		d.push({
			"action": action === 'on' ? 1 : (action === 'off' ? 0 : 2),
			"startX": parseInt(start[0]),
			"startY": parseInt(start[1]),
			"endX": parseInt(end[0]),
			"endY": parseInt(end[1])
		});
	});
	return d;
}

function getInitialLightArray() {
	let lights = [];
	for (let i = 0; i < 1000; i++) {
		lights.push(new Array(1000).fill(0));
	}
	return lights;
}

function partOne(data) {
	let lights = getInitialLightArray();
	data.forEach(d => {
		for (let y = d.startY; y <= d.endY; y++) {
			for (let x = d.startX; x <= d.endX; x++) {
				lights[x][y] = d.action === 2 ? (lights[x][y]+1) % 2 : d.action;
			}
		}
	});
	return lights.flat().reduce((a,b) => a + b);
}

function partTwo(data) {
	let lights = getInitialLightArray();
	data.forEach(d => {
		for (let y = d.startY; y <= d.endY; y++) {
			for (let x = d.startX; x <= d.endX; x++) {
				lights[x][y] += d.action === 0 ? -1 : d.action;
				lights[x][y] = Math.max(0, lights[x][y]);
			}
		}
	});
	return lights.flat().reduce((a,b) => a + b);
}

module.exports = { run, parseData, partOne, partTwo }
