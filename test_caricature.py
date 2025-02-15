import torch
from caricaturegan import CaricatureGAN
from PIL import Image
import torchvision.transforms as transforms

# Load model
model = CaricatureGAN()
model_path = "C:/Users/cj/Documents/VScode/AI_Caricature_Designer/models/caricatureGAN"  # Update this
model.load_state_dict(torch.load(model_path, map_location="cpu"))
model.eval()

# Load an image
image_path = "generated_image.png"  # Change to an actual image file
image = Image.open(image_path).convert("RGB")
transform = transforms.Compose([transforms.Resize((256, 256)), transforms.ToTensor()])
image = transform(image).unsqueeze(0)

# Generate caricature
with torch.no_grad():
    output = model(image)

print("Caricature generated successfully!")
