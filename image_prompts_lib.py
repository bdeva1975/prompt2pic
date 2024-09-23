import os
from openai import OpenAI
from io import BytesIO
import requests
from random import randint
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def get_image_from_model(prompt_content, negative_prompt=None):
    # Combine prompt and negative prompt
    full_prompt = prompt_content
    if negative_prompt:
        full_prompt += f" Negative prompt: {negative_prompt}"

    try:
        response = client.images.generate(
            model="dall-e-3",  # You can change this to "dall-e-2" if needed
            prompt=full_prompt,
            size="1024x1024",  # DALL-E 3 supports 1024x1024, 1792x1024, or 1024x1792
            quality="standard",  # You can change this to "hd" for DALL-E 3
            n=1,  # Number of images to generate
        )

        # Get the image URL
        image_url = response.data[0].url

        # Download the image
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            return BytesIO(image_response.content)
        else:
            raise Exception(f"Failed to download image: HTTP {image_response.status_code}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    prompt = "A beautiful landscape with mountains and a lake"
    negative_prompt = "No people, no buildings"
    
    image_bytes = get_image_from_model(prompt, negative_prompt)
    
    if image_bytes:
        # Save the generated image
        with open("generated_image.png", "wb") as f:
            f.write(image_bytes.getvalue())
        print("Image generated and saved as 'generated_image.png'")
    else:
        print("Failed to generate image")