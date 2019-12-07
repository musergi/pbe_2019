<?php
$uid = $_GET['uid'];
require_once __DIR__ . '/../auth.php';
$student = get_student($uid);
echo assoc_to_csv($student);

function assoc_to_csv($array) {
    return implode(',', array_keys($array)) . "\n" . implode(',', array_values($array)) . "\n";
}
?>