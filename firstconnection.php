<?php
// Connecting, selecting database
$dbconn = pg_connect("host=192.168.1.186 dbname=template0 user=posgres password=centodigiotto")
    or die('Could not connect: ' . pg_last_error());
    
    echo "\n Connessione riuscita"
    
>

