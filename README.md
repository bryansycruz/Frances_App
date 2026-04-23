# Français Fácil 🇫🇷

Aplicación web interactiva para aprender las **combinaciones de letras y vocales del francés** con mnemotecnias, emojis, audio y juegos. Pensada para hispanohablantes que apenas empiezan.

![Francés Fácil](https://img.shields.io/badge/idioma-español-blue) ![Francés](https://img.shields.io/badge/aprende-francés-red) ![Sin instalación](https://img.shields.io/badge/sin-instalación-green)

---

## ✨ ¿Qué trae?

- **Explorar** — 27 combinaciones con colores, emojis, ejemplos y trucos de memoria
- **Flashcards** — Tarjetas que voltean para repasar
- **Quiz de sonido** — Adivina cómo suena una combinación
- **Quiz de palabra** — Escucha una palabra y adivina qué combinación tiene
- **Escribir** — Dictado: escuchas y escribes
- **🎨 Visual** — Cada palabra con su emoji (el cerebro recuerda mejor con imágenes)
- **🎮 Parejas** — Juego de memoria emparejando emojis con palabras
- **🏆 Retos** — 6 desafíos: Relámpago ⚡, Puntería Perfecta 🎯, Oído Francés 👂, Memoria 🧠, Maratón Mixto 🔥 y Reto Diario 📅

Todo el progreso (puntos, récords, palabras dominadas) se guarda en tu navegador.

---

## 🚀 Cómo usar (súper fácil, sin instalar nada)

### Opción 1: La más simple — doble clic ⭐ RECOMENDADO

1. Descarga el proyecto desde GitHub:
   - Botón verde **`Code` → `Download ZIP`**
   - Extrae la carpeta ZIP donde quieras
2. Entra a la carpeta y **haz doble clic en `abrir.bat`**
   *(o haz doble clic directamente en `index.html`)*
3. ¡Listo! Se abre en tu navegador.

**No necesitas instalar nada más.** Ni Python, ni Node, ni librerías. La app es 100% HTML + JavaScript y funciona sin internet.

### Opción 2: Con Python (opcional — solo si Opción 1 falla con el audio)

Algunos navegadores bloquean el micrófono/audio cuando se abre un archivo local directamente. Si el botón 🔊 no suena, corre un servidor local:

```bash
python servidor.py
```

Luego abre en tu navegador: `http://localhost:8000`

---

## 🔊 Para que funcione el audio (pronunciación en francés)

La app usa la voz francesa que tu sistema tenga instalada. Si no escuchas nada:

### En Windows 10/11

1. **Configuración** → **Hora e idioma** → **Idioma**
2. **Agregar un idioma** → busca **"Francés (Francia)"** → Instalar
3. Al instalarlo, marca también la opción de **"Texto a voz"**
4. Reinicia el navegador

### Navegador recomendado

- ✅ **Google Chrome** o **Microsoft Edge** (mejor soporte de voz)
- ⚠️ Firefox a veces no tiene voz francesa instalada

---

## 📁 Estructura del proyecto

```text
frances_App/
├── index.html       ← La aplicación completa (todo en un archivo)
├── abrir.bat        ← Doble clic para abrir en Windows
├── servidor.py      ← Servidor local opcional (solo si fallara el audio)
├── README.md        ← Este archivo
├── LICENSE          ← Licencia MIT (libre)
└── .gitignore
```

**Nota:** No hay carpetas `node_modules`, `venv`, ni archivos extraños. Todo está en un solo `index.html` para que sea fácil de entender y modificar.

---

## 🛠️ Requisitos

| Lo que necesitas | ¿Por qué? |
| --- | --- |
| Un navegador moderno (Chrome, Edge, Firefox) | Para abrir la app |
| Voz francesa instalada en Windows | Para escuchar las palabras |
| **(Opcional)** Python 3.x | Solo si quieres usar el servidor local |

❌ **NO necesitas:** instalar librerías con `pip`, `npm install`, ni configurar nada.

---

## 🐛 Problemas comunes

**"El audio no suena"**
→ Instala la voz francesa en Windows (ver arriba) y reinicia el navegador.

**"Se abre el archivo pero se ve raro"**
→ Actualiza tu navegador a una versión reciente (2022 o más nueva).

**"El progreso se borra"**
→ Revisa que el navegador no esté en modo incógnito / privado.

**"Quiero reiniciar todo mi progreso"**
→ Abre la consola del navegador (F12), pestaña "Consola" y escribe:

```js
localStorage.clear(); location.reload();
```

---

## 💡 Consejos para aprender mejor

1. **Empieza por "Explorar"** — lee cada mnemotecnia con calma
2. **Usa el botón 🔊** en cada palabra para entrenar el oído
3. **Flashcards 10 minutos al día** es mejor que 1 hora una vez por semana
4. **Reto Diario** — hazlo cada día para mantener una racha 🔥
5. Cuando te sientas lista, prueba **Maratón Mixto 🔥**

---

## 🔒 Seguridad

Este proyecto fue revisado con las siguientes medidas:

- ✅ **Cero dependencias externas.** No se cargan CDNs, fuentes ni scripts de terceros → sin riesgo de cadena de suministro.
- ✅ **Sin conexiones de red.** La app no envía datos a ningún servidor. Todo se guarda localmente en `localStorage` del navegador (solo progreso, sin datos personales).
- ✅ **Content Security Policy (CSP)** activa en `index.html` que bloquea scripts externos, iframes, formularios y recursos remotos.
- ✅ **Escape de HTML** en todo contenido dinámico insertado en el DOM — previene XSS incluso si se modifica la lista de palabras.
- ✅ **Sin `eval`, sin `document.write`, sin `onclick` inline con datos** — listeners delegados con atributos `data-*`.
- ✅ **Servidor local restringido a `127.0.0.1`.** Si usas `servidor.py`, **no** se expone a otros dispositivos de la red Wi-Fi.
- ✅ **Cabeceras de seguridad** en el servidor: `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, `Cache-Control`.
- ✅ **Licencia MIT** — código abierto y auditable.

Si encuentras un problema de seguridad, por favor abre un issue en GitHub.

---

## 📝 Licencia

MIT — Úsalo, modifícalo y compártelo libremente.

**Bonne chance et amusez-vous!** 🎉
