<!DOCTYPE html>
<html>
<head>
    <?php
    $title = "Admin";
    include('admin_head.php');
    ?>
</head>
<body>
    <?php
        $header_content = "Admin";
        include('page_header.php');
    ?>
    <div class="container">
        <h3>Tables</h3>
        <ul class="table-list">
            <?php
            $table_url = '/admin/table.php';
            $table_names = array(
//                'admins',
                'users',
                'students',
                'timetables',
                'marks',
                'tasks'
            );

            foreach($table_names as $table_name) {
                $link = $table_url . '?' . http_build_query(array('table_name'=>$table_name));
                echo "<a href='" . $link . "'><li>" . ucfirst($table_name) . "</li></a>";
            }
            ?>
        </ul>
    </div>
</body>