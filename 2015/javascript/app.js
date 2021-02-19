let express = require('express');
let path = require('path');

let app = express();

app.use(express.static(path.join(__dirname, 'static')))

app.get('/', function (req, res) {
	res.sendFile(path.resolve(__dirname, 'index.html'));
});

app.get('/day/:day/part/:part', function(req, res) {
	res.setHeader('Content-Type', 'application/json');

	let p = path.join(__dirname, 'day' + req.params.day + '/puzzle');
	let puzzle = require(p);
	res.json(puzzle.run(parseInt(req.params.part)));
});

app.listen(3000, function () {
	console.log('Example app listening on port 3000!');
});
