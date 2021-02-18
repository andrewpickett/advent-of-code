function runWithTimer(f, data) {
	let start = Date.now()
	let result = f(data)
	let end = Date.now()

	return result + ' -- ' + (end-start) + ' ms'

}
