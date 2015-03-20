/**
 * Created by Mike on 2015/3/19.
 */

var http = require('http');

http.createServer(function (request, response) {
  response.writeHead(200, {'Content-Type': 'text/plain'});
  response.end('Hello World\n');
}).listen(8888);

console.log('Server running at http://127.0.0.1:8888/');
