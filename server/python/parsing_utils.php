<?php
function parse_restrictions() {
    $restriction_strings = array();
    foreach ($_GET as $param_name => $param_value) {
        if (!is_reserved_param($param_name)) {
            $restriction = get_restriction_string($param_name, $param_value);
            array_push($restriction_strings, $restriction);
        }
    }
    add_special_restriction($restriction_strings);

    if (empty($restriction_strings)) {
        return '';
    }
    return ' WHERE ' . implode(' AND ', $restriction_strings);
}

function is_reserved_param($name) {
    $reserved_param = array(
        'table_name',
        'limit',
        'student_id'
    );
    return in_array($name, $reserved_param);
}

function get_restriction_string($name, $value) {
    $column_name = get_col_name($name);
    $comparison = get_symbol($name);
    return $column_name . $comparison . $value;
}

function get_col_name($string) {
    $open_bracket_pos = strpos($string, '(');
    if ($open_bracket_pos === FALSE) {
        return $string;
    }
    return substr($string, 0, $open_bracket_pos);
}

function add_special_restriction(& $restrictions) {
    if ($_GET['table_name'] == 'marks') {
        array_push($restrictions, 'student=' . $_GET['student_id']);
    }
}

function get_symbol($string) {
    $opening_bracket_pos = strpos($string, '(');
    $closing_bracket_pos = strpos($string, ')');
    $symbol_string = substr(
        $string,
        $opening_bracket_pos + 1,
        $closing_bracket_pos - $opening_bracket_pos - 1
    );

    switch ($symbol_string) {
        case 'lt': return '<';
        case 'lte': return '<=';
        case 'gt': return '>';
        case 'gte': return '>=';
        default: return '=';
    }
}

function parse_ordering() {
    return ' ORDER BY ' . get_ordering_cols();
}

function get_ordering_cols() {
    switch ($_GET['table_name']) {
        case 'timetables': return 'day, hour';
        case 'marks': return 'subject';
        case 'tasks': return 'tasks';
        default: return '';
    }
}

function parse_limit() {
    if ($_GET['limit'] == null) {
        return '';
    }
    return ' LIMIT ' . $_GET['limit'];
}

function is_diplayable_col($col) {
    $banned_cols = array(
        'id',
        'student'
    );
    echo !in_array($col->name, $banned_cols);
    return !in_array($col->name, $banned_cols);
}

function get_name(& $col) {
    $col = $col->name;
}

function query_to_csv($query_result) {
    $cols = mysqli_fetch_fields($query_result);
    $cols = array_filter($cols, "is_diplayable_col");
    array_walk($cols, "get_name");
    
    $csv_string = implode(",", $cols) . "\n";
    while($row = mysqli_fetch_assoc($query_result)){
        $data = array();
        foreach ($cols as $col) {
            array_push($data, $row[$col]);
        }
        $csv_string = $csv_string . implode(",", $data) . "\n";
    }

    return $csv_string;
}
?>