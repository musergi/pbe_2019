<table width="100%" class="query-table">
    <thead>
        <tr>
        <?php
        while($field = mysqli_fetch_field($result)) {
            echo "<th>" . strtoupper($field->name) . "</th>";
        }
        ?>
        </tr>
    </thead>
    <tbody>
    <?php
    while($row = mysqli_fetch_assoc($result)) {
        echo "<tr>";
        foreach ($row as $col) {
            echo "<td>" . $col . "</td>";
        }
        echo "</tr>";
    }
    ?>
    </tbody>
</table>