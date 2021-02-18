function parseData(data) {
	return data.trim();
}

function partOne(data) {
	return (data.match(/\(/g) || []).length - (data.match(/\)/g) || []).length;
}

function partTwo(data) {
	let curr_floor = 0
	for (let i = 0; i < data.length; i++) {
		curr_floor += data.charAt(i) === '(' ? 1 : -1;
		if (curr_floor < 0) {
			return i + 1;
		}
	}
}
