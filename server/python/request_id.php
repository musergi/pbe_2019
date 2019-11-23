<?php

require_once '../database/database.php';
$connection = access_database();

//Get the uid from the database
$sql = 'SELECT id, name, surname, uid FROM students WHERE uid="' . $_GET['uid'] . '";';
$result = mysqli_query($connection, $sql);

//If exits return al the data, else ERROR
if(mysqli_num_rows($result) > 0){
    echo "id,name,surname,uid\n";
    $row = mysqli_fetch_assoc($result);
    echo $row["id"].",".$row["name"].",".$row["surname"].",".$row["uid"]."\n";
}else{
    header("HTTP/1.0 404 Not Found");
}


mysqli_close($connection);
?>