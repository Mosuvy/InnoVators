import machine
from machine import Pin
import dht
import time
import network
import ubinascii
from umqtt.simple import MQTTClient
import urequests

# Konfigurasi-konfigurasi
WIFI_SSID = "wifi nenek nisah"
WIFI_PASSWORD = "bubul2021"
UBIDOTS_TOKEN = "BBUS-rJp1EB8VsJRM5aYmuqYpJFiMFmILFn"
DEVICE_LABEL = "esp32"
VARIABLE_LABEL_1 = "temperature"
VARIABLE_LABEL_2 = "humidity"
API_URL = "http://192.168.18.7:5000/sensor-data"

# Inisialisasi sensor DHT11
dht_sensor = dht.DHT11(Pin(4))

# Fungsi untuk menghubungkan ke WiFi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Menghubungkan ke WiFi...")
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        while not wlan.isconnected():
            pass
    print("WiFi terhubung:", wlan.ifconfig())

# Fungsi untuk mengirim data ke Ubidots
def send_to_ubidots(temperature, humidity):
    try:
        CLIENT_ID = ubinascii.hexlify(machine.unique_id()).decode()
        client = MQTTClient(CLIENT_ID, "industrial.api.ubidots.com", 1883, user=UBIDOTS_TOKEN, password="")
        client.connect()
        payload = '{"%s": %s, "%s": %s}' % (VARIABLE_LABEL_1, temperature, VARIABLE_LABEL_2, humidity)
        client.publish(f"/v1.6/devices/{DEVICE_LABEL}", payload)
        client.disconnect()
        print(f"Data terkirim ke Ubidots: Temp={temperature}, Hum={humidity}")
    except Exception as e:
        print("Gagal mengirim ke Ubidots:", e)

# Fungsi untuk mengirim data ke API Flask
def send_to_api(temperature, humidity):
    payload = {"temperature": temperature, "humidity": humidity}
    try:
        response = urequests.post(API_URL, json=payload)
        print("Data terkirim ke API:", response.text)
        response.close()
    except Exception as e:
        print("Gagal mengirim data ke API:", e)

# Main loop
connect_wifi()
while True:
    try:
        time.sleep(2)
        dht_sensor.measure()
        temperature = dht_sensor.temperature()
        humidity = dht_sensor.humidity()

        send_to_ubidots(temperature, humidity)
        send_to_api(temperature, humidity)

        time.sleep(10) #Delay nya 10 detik
    except Exception as e:
        print("Error:", e)

