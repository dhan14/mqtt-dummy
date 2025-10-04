import asyncio
import gmqtt
import json
import time
import random
from datetime import datetime

# --- Konfigurasi MQTT ---
BROKER_HOST = '127.0.0.1'
BROKER_PORT = 1883
TOPIC = 'iot/sensor/data'
CLIENT_ID = 'django-mock-publisher'
# ---

async def main():
    client = gmqtt.Client(CLIENT_ID)

    try:
        #masuk ke Mosquitto di podman
        print(f"⌛ Mencoba masuk ke MQTT Broker di {BROKER_HOST}:{BROKER_PORT}")
        await client.connect(BROKER_HOST, BROKER_PORT)
        print(f"✅ Terhubung ke MQTT Broker!")
    except Exception as e:
        print(f"❌ Gagal terhubung ke MQTT Broker: Cek kontainer podman Mosquitto jalan dulu, portnya di 1883. Error: {e}")
        return

    while True:
        # Generate Data Dummy
        sensor_data = {
            "timestamp": datetime.now().isoformat(),
            # Suhu: float antara 20.0 dan 35.0
            "temperature": round(random.uniform(20.0, 35.0), 2),
            # Kelembaban: integer antara 40 dan 90
            "humidity": random.randint(40, 90),
            # Tekanan: float antara 980.0 dan 1020.0
            "pressure": round(random.uniform(980.0, 1020.0), 2)
        }

        payload = json.dumps(sensor_data)

        # Publish ke Topik
        client.publish(TOPIC, payload, qos=1)

        print(f"➡️ Kirim ke '{TOPIC}': {payload}")

        # Tunggu 5 detik
        await asyncio.sleep(5)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nPublisher dihentikan.")
