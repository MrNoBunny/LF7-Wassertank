<?php
function pumpen() {
    $sock = socket_create(AF_INET, SOCK_DGRAM, SOL_UDP);
    $server_ip = '192.168.123.20';
    $server_port = 2222;
    socket_connect($sock, $server_ip, $server_port);
    $befehl = 'PUMPEN';
    socket_send($sock, $befehl, strlen($befehl), 0);
    sleep(5);
    $befehl = 'STOPP';
    socket_send($sock, $befehl, strlen($befehl), 0);
}

if (isset($_POST['pumpen'])) {
    pumpen();
}

header("Location: index.php");
exit;
?>
