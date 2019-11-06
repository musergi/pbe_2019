<?php
    session_start();
    require_once 'auth.php';
    if (is_authenticated()) {
        include('templates/home.php');
    } else {
        include('templates/authentication.php');
    }
?>
