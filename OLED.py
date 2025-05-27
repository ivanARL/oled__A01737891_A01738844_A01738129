from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import time

i2c = busio.I2C(SCL, SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

disp.fill(0)
disp.show()

width = disp.width
height = disp.height

def imprimeNombres(texto):
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    
    time.sleep(2)
    draw.text((15, 20), texto, font=font, fill=255)
    disp.image(image)
    disp.show()
    
imprimeNombres("Bruno, Ivan y Omar")
time.sleep(2)

mensaje = input("Escribe un mensaje (máximo 50 caracteres): ")
mensaje = mensaje[:50]  # Limitar a 50 caracteres

imprimeNombres(mensaje)
time.sleep(3)
