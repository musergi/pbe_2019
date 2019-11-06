<?php
    session_start();

    if ($_SERVER["REQUEST_METHOD"] != "POST") {
        header('Location: /admin', 302);
    }

    // Auth and redirect
    require_once 'auth.php';

    if (is_authenticated()) {
        header('Location: /admin/home.php', 302);
    }

    $err = authenticate($_POST['username'], $_POST['password']);
    header('Location: /admin', 302);

    mysqli_close($connection);
?>