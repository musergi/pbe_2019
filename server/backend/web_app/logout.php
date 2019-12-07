<?php
    session_start();
    require_once '../auth.php';
    logout();
    header('Location: /', 302);
?>