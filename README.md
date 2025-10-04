# mqtt-dummy
Server MQTT dummy untuk latihan 

## Aturan pakai

## Pull image
Pull image di tools kontainer kesayangan kalian mau docker atau podman bebas, tapi TS disini pake podman

```
podman pull eclipse-mosquitto
```

### Bikin Kontainernya:
```
podman run -d \
  --name mqtt-broker \
  -p 1883:1883 \
  -v ./mosquitto.conf:/mosquitto/config/mosquitto.conf \> 
  eclipse-mosquitto
```

### Eksekusi dah
```
python3 mqtt_dummy_pub.py
```

## Hasilnya
```
⌛ Mencoba masuk ke MQTT Broker di 127.0.0.1:1883
✅ Terhubung ke MQTT Broker!
➡️ Kirim ke 'iot/sensor/data': {"timestamp": "2025-10-04T23:52:47.141474", "temperature": 32.6, "humidity": 60, "pressure": 1004.69}
➡️ Kirim ke 'iot/sensor/data': {"timestamp": "2025-10-04T23:52:52.145586", "temperature": 30.22, "humidity": 48, "pressure": 985.62}
➡️ Kirim ke 'iot/sensor/data': {"timestamp": "2025-10-04T23:52:57.149739", "temperature": 29.79, "humidity": 86, "pressure": 990.51}
➡️ Kirim ke 'iot/sensor/data': {"timestamp": "2025-10-04T23:53:02.156396", "temperature": 27.41, "humidity": 57, "pressure": 994.31}
➡️ Kirim ke 'iot/sensor/data': {"timestamp": "2025-10-04T23:53:07.161604", "temperature": 33.15, "humidity": 65, "pressure": 991.81}
^C
Publisher dihentikan.
```
