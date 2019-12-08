<?php
function parse_query($student, $query) {
    $query_parts = preg_split('/[&?]/', $query);
    $table_name = array_shift($query_parts);
    $where_statment = parse_where($table_name, $student, $query_parts);
    $order_statment = parse_order($table_name);
    $limit_statment = parse_limit($query_parts);
    return "SELECT * FROM $table_name $where_statment $order_statment $limit_statment;";
}
function parse_where($table, $student, $fragments) {
    $restrictions = array();
    foreach ($fragments as $frag) {
        $name = first_match('/([a-z]+)(?=[[(=])/i', $frag);
        if ($name == 'limit') continue;
        $comparison = to_symbol(first_match('/(?<=[[(])([glte]+)(?=[\]\)])/', $frag));
        $value = get_value($frag);
        array_push($restrictions, $name . $comparison . $value);
    }
    add_spetial_restrictions($table, $student, $restrictions);
    return !empty($restrictions) ? ' WHERE ' . implode(' AND ', $restrictions) : '';
}
function add_spetial_restrictions($table, $student, &$restrictions) {
    if ($table == "tasks") array_push($restrictions, "date>NOW()");
    if ($table == "marks") array_push($restrictions, "student=" . $student);
}
function to_symbol($string) {
    switch($string) {
        case 'lte': return '<=';
        case 'lt': return '<';
        case 'gte': return '>=';
        case 'gt': return '>';
        default: return '=';
    }
}
function get_value($string) {
    $value = first_match('/(?<=[=])(.+)/i', $string);
    $value = $value == "now" ? "NOW()" : $value;
    return is_numeric($value) ? $value : '"' . $value . '"';
}
function first_match($regex, $subject) {
    $matches = array();
    preg_match_all($regex, $subject, $matches);
    return array_shift(array_shift($matches));
}
function parse_order($table) {
    switch ($table) {
        case 'timetables': return 'ORDER BY CASE WHEN day=WEEKDAY(NOW()) AND hour>TIME(NOW()) THEN 0 WHEN day>WEEKDAY(NOW()) THEN 1 ELSE 2 END';
        case 'marks': return 'ORDER BY subject';
        case 'tasks': return 'ORDER BY date';
        default: return '';
    }
}
function parse_limit($fragments) {
    foreach ($fragments as $frag)
        if($val = first_match('/(?<=limit=)(.+)/i', $frag))
            return "LIMIT $val";
    return '';
}

function query_to_csv($result) {
    $col_names = array();
    while ($col = mysqli_fetch_field($result)) {
        if ($col->name != "id" && $col->name != "student") {
            array_push($col_names, $col->name);
        }
    }
    $content = '';
    while ($row = mysqli_fetch_array($result)) {
        $row_elements = array();
        foreach ($col_names as $item) {
            array_push($row_elements, $item != 'day' ? $row[$item] : get_weekday($row[$item]));
        }
        $content = $content . implode($row_elements) . "\n";
    }
    return implode(",", $col_names) . "\n" . $content;
}
function get_weekday($index) {
    switch ($index) {
        case 0: return 'Monday';
        case 1: return 'Tuesday';
        case 2: return 'Wednesday';
        case 3: return 'Thursday';
        case 4: return 'Friday';
        case 5: return 'Saturday';
        case 6: return 'Sunday';
        default: return 'None';
    }
}
?>