<?php
require_once '../auth.php';
$user_id = get_user($_POST['username'], $_POST['password']);
if ($user_id === FALSE) {
    header("HTTP/1.0 404 Not Found");
}
echo "$user_id," . $_POST['username'];
?>