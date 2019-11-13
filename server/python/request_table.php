<?php

require_once '../database/database.php';
$connection = access_database();

$table_name = $_GET("table_name");

switch($table_name){
    case 'tasks' :
        $sql = 'SELECT date, subject, name FROM tasks;';
        $result = mysqli_query($connection, $sql);
        if(mysqli_num_rows($result)>0){
            echo "date,subject,name<br>";
            while($row = $result->fetch_assoc()){
                echo $row["date"].",".$row["subject"].",".$row["name"]."<br>";
            }
        }else{
            header("HHTP/1.0 404 Not Found");
        }
        break;
    case 'marks' :
        $sql = 'SELECT subject, name, mark FROM marks WHERE student="' .$_GET['id'].'";';
        $result = mysqli_query($connection, $sql);
        if(mysqli_num_rows($result)>0){
            echo "subject,name,mark<br>";
            while($row = $result->fetch_assoc()){
                echo $row["subject"].",".$row["name"].",".$row["mark"]."<br>";
            }
        } else {
            header("HHTP/1.0 404 Not Found");
        }
        break;
    case timetables :
        $sql = 'SELECT day, hour, subject, room FROM timetables;';
        $result = mysqli_query($connection, $sql);
        if(mysqli_num_rows($result)>0){
            echo "day,hour,subject,room<br>";
            while($row = $result->fetch_assoc()){
                echo $row["day"].",".$row["hour"].",".$row["subject"].",".$row["room"]."<br>";
            }
        }else{
            header("HHTP/1.0 404 Not Found");
        }
        break;
    default: 
        header("HHTP/1.0 404 Not Found");
        break;
}

mysqli_close($connection);


?>