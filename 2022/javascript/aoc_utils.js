function runWithTimer(f, data) {
	let start = Date.now()
	let result = f(data)
	let end = Date.now()

	return { "result": result, "millis": (end-start) }
}

function permutator(inputArr) {
	let result = [];

	const permute = (arr, m = []) => {
		if (arr.length === 0) {
			result.push(m)
		} else {
			for (let i = 0; i < arr.length; i++) {
				let curr = arr.slice();
				let next = curr.splice(i, 1);
				permute(curr.slice(), m.concat(next))
			}
		}
	}
	permute(inputArr)
	return result;
}

module.exports = { runWithTimer, permutator }
