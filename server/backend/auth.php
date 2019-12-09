<?php
function is_auth() { return $_SESSION['is_auth'] != null ? $_SESSION['is_auth'] : FALSE;}
function authenticate($username, $password) {
    require_once __DIR__ . '/../database/database.php';
    $result = mysqli_query(access_database(), "SELECT password, salt, student FROM users WHERE username=\"$username\";");
    if ($result == FALSE || mysqli_num_rows($result) == 0) return FALSE;
    $assoc = mysqli_fetch_assoc($result);
    $hash = hash("sha256", $password . $assoc['salt']);
    if ($hash == $assoc['password']) {
        $_SESSION['username'] = $username;
        $_SESSION['student'] =  $assoc['student'];
        $_SESSION['is_auth'] = TRUE;
    }
}
function logout() {
    $_SESSION['username'] = null;
    $_SESSION['student'] =  null;
    $_SESSION['is_auth'] = FALSE;
}
function get_user($username, $password) {
    require_once __DIR__ . '/../database/database.php';
    $result = mysqli_query(access_database(), "SELECT id, password, salt FROM users WHERE username=\"$username\";");
    if ($result == FALSE || mysqli_num_rows($result) == 0) return FALSE;
    $assoc = mysqli_fetch_assoc($result);
    $hash = hash("sha256", $password . $assoc['salt']);
    if ($hash == $assoc['password']) {
        return $assoc['id'];
    }
    return FALSE;
}
function get_student($uid) {
    require_once __DIR__ . '/../database/database.php';
    $student_query = query_database("SELECT * FROM students WHERE uid=\"$uid\"");
    if ($student_query === FALSE || mysqli_num_rows($student_query) == 0) return FALSE;
    return mysqli_fetch_assoc($student_query); 
}
function get_student_from_user($username, $password) {
    require_once __DIR__ . '/../database/database.php';
    $result = query_database("SELECT * FROM users WHERE username=\"$username\"");
    if ($result === FALSE || mysqli_num_rows($result) == 0) return FALSE;
    $assoc = mysqli_fetch_assoc($result);
    $hash = hash("sha256", $password . $assoc['salt']);
    if ($hash != $assoc['password']) {
        return FALSE;
    }
    $result = query_database("SELECT * FROM students WHERE id=" . $assoc['student'] . ";");
    if ($result === FALSE || mysqli_num_rows($result) == 0) return FALSE;
    return mysqli_fetch_assoc($result);
}
?>