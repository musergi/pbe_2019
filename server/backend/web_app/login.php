<?php
    session_start();
    require_once '../auth.php';
    authenticate($_POST['username'], $_POST['password']);
    header('Location: /', 302);
?>