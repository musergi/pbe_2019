<?php
    session_start();
    require_once 'backend/auth.php';
    if (is_auth()) {
        $table = '';
        if ($_SERVER['REQUEST_METHOD'] == "POST") {
            require_once 'database/database.php';
            require_once 'backend/web_app/parse.php';
            $result = mysqli_query(access_database(), parse_request($_POST['query']));
            $table = render_query($result);
        }
        include('query.php');
    } else {
        include('login_page.html');
    }
?>