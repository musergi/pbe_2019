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

$cols = implode(",", $fields);
$user_query = $user_query . $cols . ' FROM ' . $_GET["table_name"] .' ';

// Where contraint
$where_inserted = FALSE;
foreach($_GET as $key => $value) {
    echo $key . "," . $value . "\n";
    if ($key == 'table_name' || $key == 'limit' || $key == 'student_id') {
        continue;
    }

    if (!$where_inserted) {
        $user_query = $user_query . ' WHERE ';
        $where_inserted = TRUE;
    } else {
        $user_query = $user_query . ' AND ';
    }

    $starting_pos = strpos($key, '(');
    $ending_pos = strpos($key, ')');
    $restriction_type = substr($key, $starting_pos + 1, $ending_pos - $starting_pos - 2);
    $variable_name = $key;
    if ($starting_pos !== FALSE) {
        $variable_name = substr($key, 0, $starting_pos);
    }
    echo $name_end;
    $user_query = $user_query . $variable_name;
    switch ($restriction_type) {
        case 'gt':
            $user_query = $user_query . '>';
            break;
        case 'gte':
            $user_query = $user_query . '>=';
            break;
        case 'lt':
            $user_query = $user_query . '<';
            break;
        case 'lte':
            $user_query = $user_query . '<=';
            break;
        default:
            $user_query = $user_query . '=';
    }
    $user_query = $user_query . $value;
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

echo $user_query . "\n";

$result = mysqli_query($connection, $user_query);
if(mysqli_num_rows($result)>0){
    echo $cols . "\n";
    while($row = $result->fetch_assoc()){
        $data = array();
        foreach ($fields as $field) {
            array_push($data, $row[$field]);
        }
        echo implode(",", $data) . "\n";
    }
} else {
    header("HHTP/1.0 404 Not Found");
}

?>