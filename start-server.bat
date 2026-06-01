@echo off
cd /d "%~dp0"
echo.
echo  Сервер для Unity WebGL
echo  ======================
echo  Квест: http://localhost:8080/kvest_web_stor14.html
echo  Ігри:  http://localhost:8080/public/games.html
echo.
echo  Зупинити: Ctrl+C
echo.

where py >nul 2>&1 && (
  py "%~dp0scripts\serve-unity.py" 8080
  goto :end
)
where python >nul 2>&1 && (
  python "%~dp0scripts\serve-unity.py" 8080
  goto :end
)

where npx >nul 2>&1 && (
  echo  Python не знайдено — використовуємо npx serve
  npx --yes serve -l 8080 .
  goto :end
)

echo  Помилка: встановіть Python або Node.js
echo  Python: https://www.python.org/

:end
pause
