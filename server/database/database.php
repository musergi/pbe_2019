<?php
    function access_database() {
        $database_address = '127.0.0.1';
        $username = 'musergi';
        $password = 'password';
        $database_name = 'minerva_db';

        $connection = mysqli_connect(
            $database_address,
            $username,
            $password,
            $database_name);
            
        if (!$connection) {
            die("Connection failed: " . mysqli_connect_error());
        }

        return $connection;
    }
?>