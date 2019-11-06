<!DOCTYPE html>
<html style="height: 100%">
<head>
    <?php
    $title = "Admin";
    include('admin_head.php');
    ?>
</head>
<body style="height: 100%;">
    <?php
    $header_content = ucfirst($_GET['table_name']);
    include('page_header.php');
    ?>
    <?php
        if ($_GET['table_name'] == 'students')
        {
            include('db_forms/students.php');
        }
    ?>
    <?php
    include('table_from_query.php')
    ?>
</body>
</head>