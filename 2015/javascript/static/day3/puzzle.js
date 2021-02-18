function parseData(data) {
	return data.trim();
}

const DIR_MAP = {
	'>': [1, 0],
	'<': [-1, 0],
	'^': [0, 1],
	'v': [0, -1]
}

function movePosition(pos, dir) {
	pos[0] += DIR_MAP[dir][0];
	pos[1] += DIR_MAP[dir][1];
	return pos;
}

function partOne(data) {
	let curr_pos = [0, 0];
	let visited_houses = new Set();
	visited_houses.add(curr_pos[0] + ' ' + curr_pos[1]);

	for (let i = 0; i < data.length; i++) {
		let pos = movePosition(curr_pos, data.charAt(i));
		visited_houses.add(pos[0] + ' ' + pos[1]);
	}
	return visited_houses.size;
}

function partTwo(data) {
	let santa_pos = [0, 0];
	let robo_pos = [0, 0];
	let visited_houses = new Set();
	visited_houses.add(santa_pos[0] + ' ' + santa_pos[1]);
	visited_houses.add(robo_pos[0] + ' ' + robo_pos[1]);

	for (let i = 0; i < data.length; i++) {
		let pos = movePosition(i % 2 === 0 ? santa_pos : robo_pos, data.charAt(i));
		visited_houses.add(pos[0] + ' ' + pos[1]);
	}
	return visited_houses.size;
}

module.exports = { parseData, partOne, partTwo }
