<?php
require_once '../parse.php';
require_once '../../database/database.php';
$query = parse_query($_GET['id'], $_GET['query']);
echo query_to_csv(query_database($query));
?>