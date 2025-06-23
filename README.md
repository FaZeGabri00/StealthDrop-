# 🐍 StealthDrop — Implant C2 en Python

**StealthDrop** es un proyecto ofensivo educativo en Python que simula el comportamiento de un *implant* o *agente C2*.  
Es ideal para pruebas de laboratorio, entrenamiento en Red Team, o como base para construir tus propias herramientas ofensivas.

⚠️ **Este proyecto es solo para fines educativos y entornos controlados.**

---

## 📦 Características

- Comunicación con servidor C2 vía HTTP
- Callback aleatorio para evadir detección
- Ejecución de comandos remotos
- Envío de resultados codificados en Base64
- Módulo separado de configuración (`config.py`)
- Cliente multi-plataforma en Python

---

## 🧱 Estructura del Proyecto

```
StealthDrop/
├── implant.py # Cliente implant
├── server.py # Servidor C2 en Flask
├── config.py # Configuración general
```

---

## 🚀 Uso

### 🖥️ 1. Inicia el servidor C2

```bash
pip install flask
python server.py
```
El servidor escuchará en http://0.0.0.0:5000.

🧑‍💻 2. Ejecuta el implante
```
pip install requests
python implant.py
```
El implant se conectará periódicamente al servidor para pedir instrucciones.
 
📤 3. Enviar comandos al implant
En otro terminal, puedes usar curl para programar un comando:
```
curl -X POST http://localhost:5000/set -d "cmd=whoami"
```
El output del comando será enviado de vuelta y mostrado en la consola del servidor.


## ⚙️ Configuración (config.py)
```
C2_URL = "http://localhost:5000"
SLEEP_MIN = 5
SLEEP_MAX = 10
```
Puedes ajustar el intervalo de callback para hacerlo más o menos ruidoso.

## 📜 Licencia
MIT License — libre para modificar, usar y compartir.
Haz buen uso del poder, padawan ⚔️

## 🛑 Advertencia Legal
Este proyecto está destinado únicamente a uso ético y educativo.
El uso en sistemas sin autorización es ilegal.
El autor no se hace responsable de ningún uso indebido.


