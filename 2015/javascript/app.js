let express = require('express');
let path = require('path');
let fs = require('fs')

let app = express();

app.use(express.static(path.join(__dirname, 'static')))

app.get('/', function (req, res) {
	let resVal = '';
	fs.readdirSync(path.join(__dirname, 'static')).forEach(file => {
		if (!file.endsWith('.js')) {
			resVal += '<a href="/' + file + '/puzzle.html">' + file + '</a><br />';
		}
	});
	res.send(resVal)
});

app.listen(3000, function () {
	console.log('Example app listening on port 3000!');
});
