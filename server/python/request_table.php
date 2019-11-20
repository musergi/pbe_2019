<?php

require_once '../database/database.php';
$connection = access_database();

$table_name = $_GET["table_name"];

switch($table_name){
    case 'tasks' :
        $count = 0;
        $limit = $_GET['limit'];
        $date = $_GET['date'];
        $sql = 'SELECT date, subject, name FROM tasks ORDER BY date = now ';
        if($limit == null){
            $limit = 15;
        }
        if($date != null){
            $sql = 'SELECT date, subject, name FROM tasks ORDER BY date WHERE date="'.$_GET['date'].'";'; 
        }
        $result = mysqli_query($connection, $sql);
        if(mysqli_num_rows($result)>0){
            echo "date,subject,name\n";
            while($row = $result->fetch_assoc() && $limit>$count){
                echo $row["date"].",".$row["subject"].",".$row["name"]."\n";
                $count++;
            }
        }else{
            header("HHTP/1.0 404 Not Found");
        }
        break;
    case 'marks' :
<<<<<<< HEAD
        $sql = 'SELECT subject, name, mark FROM marks WHERE student="' .$_GET['student_id'].'";';
=======
        $mark = $_GET['mark'];
        $subject = $_GET['subject'];
        $sql = 'SELECT subject, name, mark FROM marks ORDER BY subject WHERE student="' .$_GET['id'].'";';
        if($mark == 5){
            $sql = 'SELECT subject, name, mark FROM marks ORDER BY subject WHERE student="' .$_GET['id'].'", mark < "'.$_GET['mark'].'";';
        }
        if($subject != null){
            $sql = 'SELECT subject, name, mark FROM marks ORDER BY subject WHERE student="' .$_GET['id'].'", subject="'.$_GET['subject'].'";';
        }
>>>>>>> Alicia
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
        $sql = 'SELECT day, hour, subject, room FROM timetables ORDER BY date = now, hour > now; ';
        if($limit == null){
            $limit = 15;
        }
        if($date != null){
            $sql = 'SELECT day, hour, subject, room FROM timetables ORDER BY date, hour > now WHERE date = "'.$_GET['date'].'"; ';
        }
        $result = mysqli_query($connection, $sql);
        if(mysqli_num_rows($result)>0){
            echo "day,hour,subject,room\n";
            while($row = $result->fetch_assoc() && $limit>$count){
                echo $row["day"].",".$row["hour"].",".$row["subject"].",".$row["room"]."\n";
                $count++;
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