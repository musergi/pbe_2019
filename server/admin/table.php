<?php
    session_start();
    require_once 'auth.php';
    if (!is_authenticated() or $_SERVER['REQUEST_METHOD'] != "GET") {
        header('Location: /admin', 302);
    }

    require_once '../database/database.php';
    $connection = access_database();
    $query = "SELECT * FROM " . $_GET['table_name'] . ";";
    $result = mysqli_query($connection, $query);

    include('templates/table_page.php');
?>