<?php
header('Content-Type: application/json');
require_once 'mock.php';

// Hijack include path
set_include_path(__DIR__ . '/dummy_lib' . PATH_SEPARATOR . __DIR__ . '/4get-repo' . PATH_SEPARATOR . get_include_path());

$raw_input = file_get_contents('php://input');
$input = json_decode($raw_input, true);

if (!$input) {
    echo json_encode(['status' => 'error', 'message' => 'Invalid JSON']);
    exit;
}

$engine = preg_replace('/[^a-z0-9_]/', '', $input['engine'] ?? '');
$page = $input['page'] ?? 'web';
$manifest = json_decode(file_get_contents(__DIR__ . '/manifest.json'), true);

if (!isset($manifest[$engine])) {
    echo json_encode(['status' => 'error', 'message' => 'Engine not found']);
    exit;
}

$engine_config = $manifest[$engine];
chdir(__DIR__ . '/4get-repo');
require_once $engine_config['file'];
$className = $engine_config['class'];
$instance = new $className();

echo json_encode($instance->getfilters($page));
