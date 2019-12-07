<!DOCTYPE html>
<html>
  <head>
    <title>Minerva</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
    html, body {height: 100%; margin: 0; font-family: Verdana, Geneva, Tahoma, sans-serif;}
    .text-center {text-align: center;}
    .bg-primary {background-color: #85A2A6;}
    .bg-secondary {background-color: #D9CEB0;}
    .bg-terciary {background-color: #F2DDB6;}
    .bg-warning {background-color: #F28444;}
    .bg-error {background-color: #D95D41;}
    .text-primary {color: #85A2A6;}
    .text-white {color: white;}
    .text-black {color: black;}
    .padded-header {margin: 0; padding: 0.5em 0em;}
    .w-100 {width: 100%}
    .w-80 {width: 79%;}
    .w-20 {width: 19%;}
    #query-entry {border: none; padding: 1em; border-radius: 5px;}
    #search-button {border:none; padding: 1em; border-radius: 5px;}
    #logout-button {text-decoration: none; color: white; background-color: #D9CEB0; padding: 0.5em 1em; border-radius: 5px; font-weight: bold;}
    .padded {padding: 1em;}
    .h-padding {padding: 0em 3em;}
    .v-margin {margin: 1em 0em;}
    table {width:100%; text-align: center; border-collapse: collapse; border: 3px solid #85A2A6;}
    th {background-color: #D9CEB0; font-size: 1.2em; padding: 0.5em 0em; border: 3px solid #85A2A6; margin: 0;}
    td {padding: 0.25em 0em;}
    </style>
  </head>
  <body class="bg-terciary">
    <header>
      <h1 class="padded-header text-center text-black bg-primary">Query</h1>
    </header>
    <div>
        <form class="padded" action="/" method="POST">
            <input id="query-entry" class="w-80" type="text" name="query" placeholder="Enter your query">
            <input id="search-button" class="w-20 bg-secondary" type="submit" value="Search">
        </form>
    </div>
    <div class="h-padding v-margin">
      <?php
      echo $table;
      ?>
    </div>
    <div class="text-center">
      <a id="logout-button" href="/backend/web_app/logout.php">Logout</a>
    </div>
  </body>
</html>