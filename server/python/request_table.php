<?php

require_once '../database/database.php';
$connection = access_database();

$table_name = $_GET["table_name"];

$query = 'SELECT ';

switch($table_name){
    case 'tasks' :
        $query = $query . 'date, subject, name';
        /*
        $count = 0;
        $limit = $_GET['limit'];
        $date = $_GET['date'];
        $sql = 'SELECT date, subject, name FROM tasks WHERE date>NOW() ORDER BY date ';
        if($limit == null){
            $limit = 15;
        }
        if($date != null){
            $sql = 'SELECT date, subject, name FROM tasks WHERE date="'.$_GET['date'].'"; ORDER BY date '; 
        }
        $result = mysqli_query($connection, $sql);
        if(mysqli_num_rows($result)>0){
            echo "date,subject,name\n";
            while(($row = $result->fetch_assoc()) && $limit>$count){
                echo $row["date"].",".$row["subject"].",".$row["name"]."\n";
                $count++;
            }
        }else{
            header("HHTP/1.0 404 Not Found");
        }
        */
        break;
    case 'marks' :
        $mark = $_GET['mark'];
        $subject = $_GET['subject'];
        $sql = 'SELECT subject, name, mark FROM marks WHERE student=' .$_GET['student_id'].' ORDER BY subject;';
        if($mark == 5){
            $sql = 'SELECT subject, name, mark FROM marks WHERE student=' .$_GET['student_id'].', mark < "'.$_GET['mark'].'"; ORDER BY subject';
        }
        if($subject != null){
            $sql = 'SELECT subject, name, mark FROM marks WHERE student=' .$_GET['student_id'].', subject="'.$_GET['subject'].'" ORDER BY subject;';
        }
        $result = mysqli_query($connection, $sql);
        if(mysqli_num_rows($result)>0){
            echo "subject,name,mark\n";
            while($row = $result->fetch_assoc()){
                echo $row["subject"].",".$row["name"].",".$row["mark"]."\n";
            }
        } else {
            header("HHTP/1.0 404 Not Found");
        }
        break;
    case 'timetables':
        $count = 0;
        $limit = $_GET['limit'];
        $date = $_GET['date'];
        $sql = 'SELECT day, hour, subject, room FROM timetables ORDER BY day; ';
        if($limit == null){
            $limit = 15;
        }
        if($date != null){
            $sql = 'SELECT day, hour, subject, room FROM timetables WHERE date = "'.$_GET['date'].'"ORDER BY date ;';
        }
        $result = mysqli_query($connection, $sql);
        if(mysqli_num_rows($result)>0){
            echo "day,hour,subject,room\n";
            while(($row = $result->fetch_assoc()) && $limit>$count){
                echo "".$row["day"].",".$row["hour"].",".$row["subject"].",".$row["room"]."\n";
                $count= $count+1;
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