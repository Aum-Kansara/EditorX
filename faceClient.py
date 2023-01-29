import requests 
from base64 import encodebytes,b64decode
from PIL import Image
import io
import matplotlib.pyplot as plt

addr = 'http://localhost:5000'
face_swap_url = addr + '/api/face_swap'

def encode_image(image_path):
    pil_img = Image.open(image_path, mode='r') 
    byte_arr = io.BytesIO()
    pil_img.save(byte_arr, format='PNG') 
    encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii') 
    return encoded_img

response = requests.post(face_swap_url,  json={'face':encode_image('static/res/Black_Adam.jpeg'),'body':encode_image('static/res/Black_Adam.jpeg')})

img = response.json()['image']
img = Image.open(img)
plt.imshow(img)