let utils = require('../aoc_utils')
let data = require('./input')

function run(part) {
	const d = parseData(data);
	return (part === 1) ? utils.runWithTimer(partOne, d) : utils.runWithTimer(partTwo, d);
}

function parseData(data) {
	return data.trim().split('\n');
}

function assign(operand, target, signals) {
	let o = getOperand(operand, signals);
	if (o !== false) {
		signals[target] = o;
		return true;
	}
	return false;
}

function not(operand, target, signals) {
	let o = getOperand(operand, signals);
	if (o !== false) {
		signals[target] = (~o) & 0xffff;
		return true;
	}
	return false;
}

function and(operand1, operand2, target, signals) {
	let o1 = getOperand(operand1, signals);
	let o2 = getOperand(operand2, signals);
	if (o1 !== false && o2 !== false) {
		signals[target] = (o1 & o2) >>> 0;
		return true;
	}
	return false;
}

function or(operand1, operand2, target, signals) {
	let o1 = getOperand(operand1, signals);
	let o2 = getOperand(operand2, signals);
	if (o1 !== false && o2 !== false) {
		signals[target] = (o1 | o2) >>> 0;
		return true;
	}
	return false;
}

function shift(operand1, operand2, isLeft, target, signals) {
	let o1 = getOperand(operand1, signals);
	let o2 = getOperand(operand2, signals);
	if (o1 !== false && o2 !== false) {
		signals[target] = isLeft ? (o1 << o2) >>> 0 : (o1 >>> o2) >>> 0;
		return true;
	}
	return false;
}

function getOperand(o, signals) {
	if (!isNaN(o)) {
		return parseInt(o);
	}
	if (o in signals) {
		return signals[o];
	}
	return false;
}

function processSignals(d) {
	let signals = []
	while (d.length > 0) {
		let idx = -1;
		for (const[i, s] of d.entries()) {
			let parts = s.split(' -> ');
			let lhs = parts[0];
			let rhs = parts[1];
			let operands = lhs.split(' ');
			let processed = false
			if (operands.length === 1) {
				processed = assign(operands[0], rhs, signals);
			} else if (parts[0].indexOf('NOT') === 0) {
				processed = not(operands[1], rhs, signals);
			} else if (parts[0].indexOf('AND') >= 0) {
				processed = and(operands[0], operands[2], rhs, signals);
			} else if (parts[0].indexOf('OR') >= 0) {
				processed = or(operands[0], operands[2], rhs, signals);
			} else if (parts[0].indexOf('LSHIFT') >= 0) {
				processed = shift(operands[0], operands[2], true, rhs, signals);
			} else if (parts[0].indexOf('RSHIFT') >= 0) {
				processed = shift(operands[0], operands[2], false, rhs, signals);
			}
			if (processed) {
				idx = i;
				break;
			}
		}
		if (idx >= 0) {
			d.splice(idx, 1);
		}
	}
	return signals['a'];
}

function partOne(data) {
	return processSignals([...data]);
}

function partTwo(data) {
	let dataCopy = [...data];
	let idx = -1;
	for (let [i, e] of dataCopy.entries()) {
		if (e.endsWith(' -> b')) {
			idx = i;
			break;
		}
	}
	dataCopy.splice(idx, 1);
	dataCopy.push(partOne([...data]) + ' -> b');
	return processSignals(dataCopy);
}

module.exports = { run, parseData, partOne, partTwo }
