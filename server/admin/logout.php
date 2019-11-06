<?php
    session_start();
    require_once 'auth.php';
    logout();
    header('Location: /admin', 302);
?>