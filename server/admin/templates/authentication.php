<!DOCTYPE html>
<html style="height: 100%">
<head>
    <?php
    $title = "Admin";
    include('admin_head.php');
    ?>
</head>
<body style="height: 100%;">
    <header>
        <h1 class="main-title">Admin</h1>
    </header>
    <div class="login-container">
    <?php
    include('user_login_form.html')
    ?>
    </div>
</body>
</head>