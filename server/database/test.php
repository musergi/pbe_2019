<?php
$servername = "127.0.0.1";
$username = "musergi";
$password = "password";

// Create connection
$conn = mysqli_connect($servername, $username, $password);

// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
echo "<a href='admin.php'>Admin page</a>";
?>