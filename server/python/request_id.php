<?php

require_once '../database/database.php';
$connection = access_database();

//Get the uid from the database
$sql = 'SELECT id, name, lastname, uid FROM students WHERE uid="' . $_GET['uid'] . '";';
$result = mysqli_query($connection, $sql);

//If exits return al the data, else ERROR
if(mysqli_num_rows($result) > 0){
    echo "id,name,lastename,uid<br>";
    echo $row["id"].",".$row["name"].",".$row[lastname].",".$row["uid"]."<br>";
}else{
    header("HHTP/1.0 404 Not Found");
}


mysqli_close($conn);

?>