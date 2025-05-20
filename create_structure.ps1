$dirs = @(
    "docker", "docker\nginx",
    "app", "app\api", "app\api\v1", "app\api\v1\endpoints", "app\api\v1\schemas",
    "app\frontend", "app\frontend\views", "app\frontend\templates", "app\frontend\static",
    "app\frontend\static\js", "app\frontend\static\css", "app\frontend\static\images",
    "app\common", "app\departments", "app\departments\sales", "app\departments\hr",
    "app\models", "app\services", "migrations", "tests", "tests\test_api", "tests\test_views", "docs"
)

foreach ($d in $dirs) {
    New-Item -ItemType Directory -Force -Path "project-root\$d"
}

$files = @(
    ".env.example", ".gitignore", "requirements.txt", "setup.py", "wsgi.py",
    "app\__init__.py", "app\config.py", "app\extensions.py",
    "app\api\__init__.py", "app\api\namespace.py", "app\api\v1\__init__.py",
    "app\api\v1\endpoints\chat.py", "app\api\v1\endpoints\auth.py", "app\api\v1\schemas\__init__.py",
    "app\frontend\views\__init__.py", "app\frontend\views\home.py",
    "app\frontend\templates\base.html", "app\frontend\templates\chat.html",
    "app\common\chatbot_core.py", "app\common\utils.py",
    "app\departments\sales\logic.py", "app\departments\hr\logic.py",
    "app\models\__init__.py", "app\services\__init__.py",
    "tests\conftest.py", "docs\openapi.yaml",
    "docker\Dockerfile", "docker\docker-compose.yml"
)

foreach ($f in $files) {
    New-Item -ItemType File -Force -Path "project-root\$f"
}

Write-Output "create_structure.ps1"
