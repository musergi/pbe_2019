<?php
    require_once '../python/parsing_utils.php';

    echo '>= --> ' . get_symbol('date(gte)') . '<br>';
    echo '<  --> ' . get_symbol('hour(lt)') . '<br>';
    echo '=  --> ' . get_symbol('name') . '<br>';

    echo 'date --> ' . get_col_name('date(gte)') . '<br>';
    echo 'hour --> ' . get_col_name('hour(lt)') . '<br>';
    echo 'name --> ' . get_col_name('name') . '<br>';

    echo get_restriction_string('date(gte)','"2019-12-10"') . '<br>';

    echo parse_restrictions() . '<br>';
?>