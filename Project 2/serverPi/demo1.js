//Program to connect the mysql database and node.js and display the database on the console
//Citation: https://www.w3schools.com/nodejs/nodejs_mysql_select.asp
//Code Submission by: Smitha Bhaskar


var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "EID",
  password: "EID",
  database: "TEMP"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
  con.query("SELECT * FROM Sensor",function (err,result,fields){
    if(err) throw err;
    console.log(result);
   }); 

setTimeout((function() {
    return process.exit(22);
}), 3000); //Function to ensure the function executes only for 3 seconds
	   //Else would go into infinite loop as a default	

});
