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
HOST = "127.0.0.1"  # solo local — nunca exponer a la red

class LocalOnlyHandler(http.server.SimpleHTTPRequestHandler):
    """Handler con cabeceras de seguridad y solo para conexiones locales."""

    def end_headers(self):
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        sys.stdout.write("[%s] %s\n" % (self.log_date_time_string(), fmt % args))

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    try:
        with socketserver.TCPServer((HOST, PORT), LocalOnlyHandler) as httpd:
            url = f"http://{HOST}:{PORT}"
            print("=" * 50)
            print("  Francais Facil - Servidor local (solo tu PC)")
            print("=" * 50)
            print(f"  Servidor corriendo en: {url}")
            print(f"  Acceso restringido a localhost (no red)")
            print(f"  Presiona Ctrl+C para detenerlo")
            print("=" * 50)
            webbrowser.open(url)
            httpd.serve_forever()
    except OSError as e:
        if getattr(e, "errno", None) == 10048 or "Address already in use" in str(e):
            print(f"El puerto {PORT} ya esta en uso.")
            print(f"Abre http://{HOST}:{PORT} en tu navegador,")
            print("o cierra el otro programa y vuelve a intentar.")
        else:
            raise
    except KeyboardInterrupt:
        print("\nServidor detenido. Hasta luego!")
        sys.exit(0)

if __name__ == "__main__":
    main()
