<?php
ini_set('memory_limit', '256M');
header('Content-Type: application/json');

require_once 'mock.php';

// Hijack include path to look in dummy_lib first, then 4get-repo
set_include_path(__DIR__ . '/dummy_lib' . PATH_SEPARATOR . __DIR__ . '/4get-repo' . PATH_SEPARATOR . get_include_path());

$raw_input = file_get_contents('php://input');
$input = json_decode($raw_input, true);
$engine = preg_replace('/[^a-z0-9_]/', '', $input['engine'] ?? '');

$manifest = json_decode(file_get_contents(__DIR__ . '/manifest.json'), true);
if (!isset($manifest[$engine])) {
    die(json_encode(['status' => 'error', 'message' => "Engine $engine not found"]));
}

$engine_config = $manifest[$engine];

// Change to 4get-repo so internal relative includes work
chdir(__DIR__ . '/4get-repo');
require_once $engine_config['file'];

$className = $engine_config['class'];
$instance = new $className();

$params = array_merge([
    's' => '', 'country' => 'us', 'nsfw' => 'yes', 'lang' => 'en'
], $input['params'] ?? []);

try {  
    // 4get engines use the 'web' method for standard searches  
    $result = $instance->web($params);    
    error_log("Hijacker result: " . print_r($result, true));   
    echo json_encode($result); 
} catch (Throwable $e) {  
    echo json_encode(['status' => 'error', 'message' => $e->getMessage()]);  
}