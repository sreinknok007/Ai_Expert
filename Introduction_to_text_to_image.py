import requests
from PIL import Image
from io import BytesIO

HF_API_KEY = "LOl"

API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-3-medium-diffusers"

def generate_image(prompt):
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {"inputs": prompt}

    print("⏳ Generating image, please wait...")
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        image.show()  # Opens the image
        image.save("generated_image.png")  # Saves it locally
        print("✅ Image saved as 'generated_image.png'")
    else:
        print(f"❌ Error {response.status_code}: {response.text}")

# Example usage
generate_image("A cute baby dragon sitting on a pile of gold, digital art")
