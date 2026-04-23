"""
Servidor local opcional para Francais Facil.

Solo necesitas este script si el audio no funciona
abriendo index.html directamente (algunos navegadores
bloquean la API de voz en archivos locales).

USO:
    python servidor.py

Luego abre http://localhost:8000 en tu navegador.

Requisitos: Python 3.x (ya viene con http.server)
No necesitas instalar NADA con pip.
"""
import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    handler = http.server.SimpleHTTPRequestHandler

    try:
        with socketserver.TCPServer(("", PORT), handler) as httpd:
            url = f"http://localhost:{PORT}"
            print("=" * 50)
            print("  Francais Facil - Servidor local")
            print("=" * 50)
            print(f"  Servidor corriendo en: {url}")
            print(f"  Presiona Ctrl+C para detenerlo")
            print("=" * 50)
            webbrowser.open(url)
            httpd.serve_forever()
    except OSError as e:
        if e.errno == 10048 or "Address already in use" in str(e):
            print(f"El puerto {PORT} ya esta en uso.")
            print(f"Abre http://localhost:{PORT} en tu navegador,")
            print("o cierra el otro programa y vuelve a intentar.")
        else:
            raise
    except KeyboardInterrupt:
        print("\nServidor detenido. Hasta luego!")
        sys.exit(0)

if __name__ == "__main__":
    main()
