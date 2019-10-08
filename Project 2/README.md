# EID Project 2- Web Client to Display Temperature and Humidity Values

Developers: Smitha Bhaskar and Shanel Wu
Instructor: Bruce Montgomery
Fall 2019, University of Colorado Boulder

## Installation Instructions
You will need two machines, one server and one client.

### Server installation: 
All software required to run Project 1 is also required here: MySQL, Matplotlib, AdaFruit_DHT, PyQt5. Additionally, install Node.jS, WebSockets (ws) for Node.js, and Tornado WebSockets web server for Python

Navigate to the `serverPi` folder. Start both WebSockets servers by running `./start_servers-ssh.sh`

### Client installation:
Navigate to the `clientPi` folder. Open `index.html` to access the web interface.

## Project Work

We have integrated the results from Project 1 to be displayed on the web application which is enabled by 2 WebSocket servers: one run on a Python Tornado server and the other on a Node.js server. 

When the IP and port of the server and client are entered on the web application, upon successful connection it should display the buttons. Buttons are included for the following functions:
-->To show the latest temp and humidity data
-->To to display the current status based on sensor readings
-->To convert the data from degree Celsius to Farenheit 
-->To test the network responsiveness

## References

1. [Node WebSockets](https://flaviocopes.com/node-websockets/)
2. [Connecting Node.js to MySQL](https://www.w3schools.com/nodejs/nodejs_mysql_select.asp) [2](https://markshust.com/2013/11/07/creating-nodejs-server-client-socket-io-mysql/) [3]( https://stackoverflow.com/questions/54606538/node-js-ws-and-mysql)
3. [JQuery documentation](https://api.jquery.com/)
4. [Python WebSockets with Tornado](https://www.tornadoweb.org/en/stable/websocket.html) [2](https://os.mbed.com/cookbook/Websockets-Server)


