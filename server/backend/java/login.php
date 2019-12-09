<?php
require_once '../auth.php';
$student = get_student_from_user($_POST['username'], $_POST['password']);
if ($student === FALSE) {
    header("HTTP/1.0 404 Not Found");
}
echo "id,name,surname\n";
echo $student['id'] . "," . $student['name'] . "," . $student['surname'] . "\n";
?>