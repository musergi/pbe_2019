<?php
//numer of times entered the server
$count_nteserver ;

class server{

    function server(){
        if ($GLOBALS['count_nteserver'] == 0){
            $GLOBALS['count_nteserver'] = 1;
            echo "hola  = 0 <br>";
            echo $count_nteserver."<br>";
        }else{
            $GLOBALS['count_nteserver']++;
            echo "hola  = mas <br>";
        }

        //$GLOBALS['count_nteserver'] = $GLOBALS['count_nteserver'] + 1;
        echo "You entered the server succesfully!<br>";
        echo "Number of times entered: ".$GLOBALS['count_nteserver'];
    }

    /*function enter_server(){
    }*/

}

$server = new server();

?>