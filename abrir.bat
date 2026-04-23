@echo off
REM ===========================================
REM  Frances Facil - Abrir la aplicacion
REM ===========================================
REM  Doble clic a este archivo para abrir la
REM  app en tu navegador predeterminado.
REM ===========================================

echo.
echo  ========================================
echo    Abriendo Francais Facil...
echo  ========================================
echo.

start "" "%~dp0index.html"

REM Si quieres usar el servidor local de Python,
REM comenta la linea de arriba (anade REM al inicio)
REM y descomenta las de abajo quitando el REM:
REM
REM echo Iniciando servidor local en http://localhost:8000
REM start "" "http://localhost:8000"
REM python "%~dp0servidor.py"

exit
