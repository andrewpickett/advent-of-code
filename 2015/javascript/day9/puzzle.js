let utils = require('../aoc_utils')
let data = require('./input')

function run(part) {
	const d = parseData(data);
	return (part === 1) ? utils.runWithTimer(partOne, d) : utils.runWithTimer(partTwo, d);
}

function parseData(data) {
	let tmp = data.trim().split('\n');
	let city_map = {};
	tmp.forEach(d => {
		let parts = d.split(' ');
		if (!city_map[parts[0]]) {
			city_map[parts[0]] = {};
		}
		if (!city_map[parts[2]]) {
			city_map[parts[2]] = {};
		}
		city_map[parts[0]][parts[2]] = parseInt(parts[4])
		city_map[parts[2]][parts[0]] = parseInt(parts[4])
	});
	return city_map;
}

function calc_route(data, is_min) {
	let cities = Object.keys(data);
	let perms = utils.permutator(cities);
	let lim = is_min ? 99999999 : 0;
	perms.forEach(perm => {
		let curr_route = 0;
		for (let i = 0; i < perm.length - 1; i++) {
			curr_route += data[perm[i]][perm[i+1]];
		}
		if ((is_min && curr_route < lim) || (!is_min & curr_route > lim)) {
			lim = curr_route;
		}
	});
	return lim;

}

function partOne(data) {
	return calc_route(data, true);
}

function partTwo(data) {
	return calc_route(data, false);
}

module.exports = { run, parseData, partOne, partTwo }
