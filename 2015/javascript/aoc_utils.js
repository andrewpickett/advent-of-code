function runWithTimer(f, data) {
	let start = Date.now()
	let result = f(data)
	let end = Date.now()

	return { "result": result, "millis": (end-start) }
}

module.exports = { runWithTimer }
