<?php
    function is_authenticated() {
        if (!isset($_SESSION['is_authenticated'])) {
            return false;
        } else {
            return $_SESSION['is_authenticated'];
        }
    }

    function authenticate($username, $password) {
        require_once '../database/database.php';
        $connection = access_database();

        $query = 'SELECT * FROM admins WHERE username="' . $username . '";';
        $result = mysqli_query($connection, $query);

        if (mysqli_num_rows($result) != 1) {
            mysqli_close($connection);
            return 1;
        }
        
        $user = mysqli_fetch_assoc($result);
        if ($_POST['password'] != $user['password']) {
            mysqli_close($connection);
            return 2;
        }

        $_SESSION['is_authenticated'] = TRUE;
        $_SESSION['user'] = $user['id'];

        mysqli_close($connection);
        return 0;
    }

    function logout() {
        $_SESSION['is_authenticated'] = FALSE;
        $_SESSION['user'] = 0;
    }
?>