<?php

require_once '../database/database.php';
$connection = access_database();

require_once 'parsing_utils.php';
$user_query = 'SELECT * FROM ' . 
            $_GET["table_name"] .
            parse_restrictions() . //returns WHERE
            parse_ordering() . //returns ORDER BY
            parse_limit() . //returns LIMIT
            ';';

$result = mysqli_query($connection, $user_query);
if ($result == FALSE || mysqli_num_rows($result) == 0) {
    header("HTTP/1.0 404 Not Found");
}

echo query_to_csv($result);
?>