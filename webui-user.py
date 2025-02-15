import torch
from diffusers import StableDiffusionPipeline
import os

# Load model (Ensure you've downloaded it)
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.to("cuda")  # Ensure CUDA is available

# Load text description
def load_description(file_path):
    with open(file_path, "r") as f:
        return f.read().strip()

# Generate image
def generate_image(prompt, output_path):
    image = pipe(prompt).images[0]  # Generate image
    image_path = os.path.join(output_path, "generated_image.png")
    image.save(image_path)
    print(f"Image saved at {image_path}")

# Main function
if __name__ == "__main__":
    input_file = "data/input_text/case1.txt"
    output_dir = "data/generated_images"
    os.makedirs(output_dir, exist_ok=True)

    prompt_text = load_description(input_file)
    generate_image(prompt_text, output_dir)
