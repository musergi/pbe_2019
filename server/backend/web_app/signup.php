<?php
if ($_POST['password'] != $_POST['password_confirmation']) echo 'Error';
$salt = bin2hex(random_bytes(10));
$hash = hash("sha256", $_POST['password'] . $salt);
$username = $_POST['username'];
require_once '../../database/database.php';
$query = "INSERT INTO users (username, password, salt) VALUES (\"$username\", \"$hash\", \"$salt\");";
echo $query;
$res = mysqli_query(access_database(), $query);
if ($res === FALSE) echo 'Query error';
?>