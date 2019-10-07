<!-- source: https://www.w3schools.com/php/php_ajax_database.asp-->
<!DOCTYPE html>
<html>
<head>
<style>
table {
    width: 100%;
    border-collapse: collapse;
}

table, td, th {
    border: 1px solid black;
    padding: 5px;
}

th {text-align: left;}
</style>
</head>
<body>

<?php
header('Access-Control-Allow-Origin: *');
$q = intval($_GET['q']);

$con = mysqli_connect('localhost','EID','EID','TEMP');
if (!$con) {
    die('Could not connect: ' . mysqli_error($con));
}

mysqli_select_db($con,"ajax_demo");
$sql="SELECT * FROM user WHERE id = '".$q."'";
$result = mysqli_query($con,$sql);

echo "<table>
<tr>
<th>Date/Time</th>
<th>Temperature in C</th>
<th>Temperature in F</th>
<th>Humidity</th>
</tr>";
while($row = mysqli_fetch_array($result)) {
    echo "<tr>";
    echo "<td>" . $row['dateandtime'] . "</td>";
    echo "<td>" . $row['TEMPERATUREinC'] . "</td>";
    echo "<td>" . $row['TEMPERATUREinF'] . "</td>";
    echo "<td>" . $row['HUMIDITY'] . "</td>";
    echo "</tr>";
}
echo "</table>";
mysqli_close($con);
?>
</body>
</html>