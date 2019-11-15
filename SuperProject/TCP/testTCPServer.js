// Run this from the command line with `node testTCPServer.js`
// echo what is sent from the Processing sketch

var net = require('net');
var fs = require('fs');

var server = net.createServer(function(socket) {
	socket.write('Echo server\r\n');
	socket.pipe(socket);
	socket.on('data', function(data) {
	    console.log("d"+ data);
	    console.log(data);
	    //fs.writeFileSync("log.txt", data, );
	    socket.write("roger that");
	});
	socket.on('connect', function(data) {
		console.log("new connection from " + socket.remoteAddress + ":" + socket.remotePort);
	});
	socket.on('error', (e) => {
		console.log(e.code);
	});
});

server.on('listening', function(data) {
		console.log("listening at ", server.address());
});
server.on('connection', function(data) {
	console.log("new connection from ");
});
server.on('error', (e) => {
	console.log(e.code);
});


console.log("starting");
server.listen(1337, '127.0.0.1');
