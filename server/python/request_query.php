<?php

require_once '../database/database.php';
$connection = access_database();

$user_query = 'SELECT ';

$fields = array();
$field_query = 'SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = "' . $_GET["table_name"] . '";';
$result = mysqli_query($connection, $field_query);
if(mysqli_num_rows($result)>0){
    while($row = $result->fetch_assoc()){
        if ($row['COLUMN_NAME'] != 'id' && $row['COLUMN_NAME'] != 'student')
        array_push($fields, $row['COLUMN_NAME']);
    }
} else {
    header("HHTP/1.0 404 Not Found");
}

$cols = implode(',', $fields);
$user_query = $user_query . $cols . ' FROM ' . $_GET["table_name"] .' ';

// Where contraint
switch($_GET["table_name"]) {
    case 'timetables':
        // TODO: 
        break;
    case 'marks':
        $user_query = $user_query . 'WHERE student=' . $_GET['student_id'];
        if($_GET['subject'] != null) {
            $user_query = $user_query . ' AND subject="' . $_GET['subject'] . '"';
        }
        if($_GET['mark'] != null && $_GET['mark'] == 5) {
            $user_query = $user_query . ' AND mark<5';
        }
        break; 
    case 'tasks':
        $user_query = $user_query . 'WHERE ';
        if ($_GET['date'] != null) {
            $user_query = $user_query . 'date="' . $_GET['date'] . '"';
        } else {
            $user_query = $user_query . 'date>NOW()';
        }
        break;
}

// Ordering
$user_query = $user_query . ' ORDER BY ';
switch($_GET["table_name"]) {
    case 'timetables':
        $user_query = $user_query . 'day, hour';
        break;
    case 'marks':
        $user_query = $user_query . 'subject';
        break; 
    case 'tasks':
        $user_query = $user_query . 'date';
        break;
}

// Limit contraint
if ($_GET['limit'] != null) {
    $user_query = $user_query . ' LIMIT ' . $_GET['limit'];
}

$user_query = $user_query . ';';

echo $user_query . '<br>';

$result = mysqli_query($connection, $user_query);
if(mysqli_num_rows($result)>0){
    echo $cols . '\n';
    while($row = $result->fetch_assoc()){
        $data = array();
        foreach ($fields as $field) {
            array_push($data, $row[$field]);
        }
        echo implode(',', $data) . '\n';
    }
} else {
    header("HHTP/1.0 404 Not Found");
}

?>