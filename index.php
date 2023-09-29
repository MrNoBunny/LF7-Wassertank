<?php
// Database connection details
$host = "localhost";  // Replace with your database host
$username = "tankadmin"; // Replace with your database username
$password = "habehunger"; // Replace with your database password
$database = "tanks"; // Replace with your database name

// Create a database connection
$connection = new mysqli($host, $username, $password, $database);

// Check if the connection was successful
if ($connection->connect_error) {
    die("Connection failed: " . $connection->connect_error);
}

// SQL query to retrieve data from the "tanks" table
$sql = "SELECT tank1, Wassermenge1, tank2, Wassermenge2, timestamp FROM tanks";

// Execute the query
$result = $connection->query($sql);

// Check if there are any rows in the result   <th></th>
if ($result->num_rows > 0) {
    echo "<table>";
    echo "<tr><th>Wasserstand 1 in cm</th><th>Wassermenge 1 in ml</th><th>Wasserstand 2 in cm</th><th>Wassermenge 2 in ml</th><th>Timestamp</th></tr>";

    // Fetch and display data
    while ($row = $result->fetch_assoc()) {
        echo "<tr><td>" . $row["tank1"] . "</td><td>" . $row["Wassermenge1"] . "</td>
              <td>" . $row["tank2"] . "</td><td>" . $row["Wassermenge2"] . "</td>
              <td>" . $row["timestamp"] . "</td></tr>";
    }

    echo "</table>";
} else {
    echo "No data available.";
}

// Close the database connection
$connection->close();

// Funktion zum Pumpen
function pumpen() {
	// UDP Socket erstellen
	$sock = socket_create(AF_INET, SOCK_DGRAM, SOL_UDP);
	// Verbindung herstellen
	$server_ip = '192.168.123.20';
	$server_port = 2222;
	socket_connect($sock,$server_ip,$server_port);
	// Befehle senden
	$befehl = 'PUMPEN';
	socket_send($sock,$befehl,strlen($befehl),0);
	sleep(5);
	$befehl = 'STOPP';
	socket_send($sock,$befehl,strlen($befehl),0);
}

if(array_key_exists('pumpen', $_POST)) {
	pumpen();
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
<style>
 .header-image {
            position: absolute;
            top: 10px;
            right: 10px;
        }
    </style>
</head>
<body>
    <img src="LF7_Logo_Ecke.png" alt="LF7" class="header-image">
	
	<form method="post">
        <input type="submit" name="pumpen" class="button" value="5 Sekunden lang pumpen" />
    </form>
    
    <?php
    // Display the data initially
    fetchData($connection);
    ?>
</body>
</html>
