<!DOCTYPE html>
<html lang="en">
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }

        h1 {
            text-align: center;
        }

        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }

        .header-image {
            margin-right: 10px;
        }

        .button {
            padding: 15px 30px;
            font-size: 18px;
            background-color: #007bff;
            color: #fff;
            border: none;
            cursor: pointer;
            border-radius: 4px;
        }

        .button:hover {
            background-color: #0056b3;
        }

        .data-table {
            width: 100%;
            border-collapse: collapse;
        }

        .data-table th, .data-table td {
            padding: 10px;
            text-align: center;
            border: 1px solid #ddd;
        }

        .data-table th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <div class="header-container">
        <h1></h1>
        <div>
            <img src="LF7_Logo_Ecke.png" alt="LF7" class="header-image">
            <form method="post" action="process.php">
                <input type="submit" name="pumpen" class="button" value="Pumpen" />
            </form>
        </div>
    </div>

    <?php
    $host = "localhost";
    $username = "tankadmin";
    $password = "habehunger";
    $database = "tanks";

    $connection = new mysqli($host, $username, $password, $database);

    if ($connection->connect_error) {
        die("Connection failed: " . $connection->connect_error);
    }

    $sql = "SELECT tank1, Wassermenge1, tank2, Wassermenge2, timestamp FROM tanks ORDER BY timestamp DESC";

    $result = $connection->query($sql);

    if ($result->num_rows > 0) {
        echo '<table class="data-table">';
        echo '<thead><tr><th>Wasserstand 1 in cm</th><th>Wassermenge 1 in ml</th><th>Wasserstand 2 in cm</th><th>Wassermenge 2 in ml</th><th>Timestamp</th></tr></thead>';
        echo '<tbody>';

        while ($row = $result->fetch_assoc()) {
            echo '<tr>';
            echo '<td>' . $row["tank1"] . '</td>';
            echo '<td>' . $row["Wassermenge1"] . '</td>';
            echo '<td>' . $row["tank2"] . '</td>';
            echo '<td>' . $row["Wassermenge2"] . '</td>';
            echo '<td>' . $row["timestamp"] . '</td>';
            echo '</tr>';
        }

        echo '</tbody>';
        echo '</table>';
    } else {
        echo "No data available.";
    }

    $connection->close();
    ?>
</body>
</html>
