<?php
    session_start();
    require_once 'backend/auth.php';
    if (is_auth()) {
        $table = '';
        if ($_SERVER['REQUEST_METHOD'] == "POST") {
            require_once 'database/database.php';
            require_once 'backend/parse.php';
            $result = query_database(parse_query($_SESSION['student'], $_POST['query']));
            if ($result !== FALSE && mysqli_num_rows($result) > 0)
                $table = query_to_html($result);
        }
        include('query.php');
    } else {
        include('login_page.html');
    }
?>