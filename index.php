<?php
header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json; charset=utf-8');
exec('python3 patramp.py');
echo json_encode([ 'status' => 'OK' ]);