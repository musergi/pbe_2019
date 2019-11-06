<?php
session_start();
require_once('../auth.php');
if (!is_authenticated()) {
    header('Location: /admin', 302);
}

if ($_SERVER["REQUEST_METHOD"] != "POST") {
    header('Location: /admin', 302);
}

require_once('../../database/database.php');
$connection = access_database();
$query = 'INSERT INTO students (name, surname, uid) VALUES ("' . $_POST['name'] . '","' . $_POST['surname'] . '","' . $_POST['uid'] . '");';
$result = mysqli_query($connection, $query);
mysqli_close($connection);
if (!$result) {
    echo $query;
    echo "Error";
}
$table_url = '/admin/table.php';
$url = $table_url . '?' . http_build_query(array('table_name'=>'students'));
header('Location: ' . $url, 302);
?>