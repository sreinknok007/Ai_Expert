import requests
from PIL import Image, ImageEnhance,ImageFilter
from io import BytesIO

HF_API_KEY = "Nah It Wont Work For You LOL"

API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-3-medium-diffusers"

def generate_image(prompt):
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response

def ppi(image):
    enhancer = ImageEnhance.Brightness(image)
    bright_image = enhancer.enhance(1.2)  # 1.2 means a 20% increase in brightness

# Enhance contrast
    enhancer = ImageEnhance.Contrast(bright_image)
    contrast_image = enhancer.enhance(1.3) 
    sfi = contrast_image.filter(ImageFilter.GaussianBlur(radius = 2))
    return sfi

print("⏳ Generating image, please wait...")
response = generate_image(input("Sya image"))
    
if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        process_img = ppi(image)
        image.show()  # Opens the image
        image.save("generated_image.png")  # Saves it locally
        print("✅ Image saved as 'generated_image.png'")
else:
        print(f"❌ Error {response.status_code}: {response.text}")

# Example usage

