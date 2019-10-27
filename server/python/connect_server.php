<?php
//numer of times entered the server
$count_nteserver;

class server{

    function server(){
        $GLOBALS['count_nteserver'] = $GLOBALS['count_nteserver'] + 1;
        echo "You entered the server succesfully!<br>";
        echo "Number of times entered: ".$GLOBALS['count_nteserver'];
    }

    function enter_server(){
        $GLOBALS['count_nteserver']++;
        echo "You entered the server succesfully!";
        echo "Number of times entered: ".$GLOBALS['count_nteserver'];
    }

}

$server = new server();

?>