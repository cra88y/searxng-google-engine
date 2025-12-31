Write-Host "--- Auditing Harness Includes ---" -ForegroundColor Cyan

$dummyPath = "sidecar/src/dummy_lib/lib"
$files = @("fuckhtml.php", "backend.php")

foreach ($file in $files) {
    if (Test-Path "$dummyPath/$file") {
        $content = Get-Content "$dummyPath/$file" -Raw
        if ($content -match "class\s+($($file -replace '.php',''))") {
            Write-Host "[FAIL] $file contains a class definition! This will cause redeclaration errors." -ForegroundColor Red
            exit 1
        } else {
            Write-Host "[PASS] $file is clean." -ForegroundColor Green
        }
    } else {
        Write-Host "[FAIL] $dummyPath/$file is missing!" -ForegroundColor Red
        exit 1
    }
}

Write-Host "--- Audit Complete: Harness includes are isolated. ---" -ForegroundColor Cyan
