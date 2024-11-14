
import os
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

def generate_alt_text(image_path):
    processor = BlipProcessor.from_pretrained('Salesforce/blip-image-captioning-base')
    model = BlipForConditionalGeneration.from_pretrained('Salesforce/blip-image-captioning-base')
    image = Image.open(image_path).convert('RGB')
    inputs = processor(image, return_tensors='pt')
    outputs = model.generate(**inputs, max_length=60, num_beams=5, early_stopping=True)
    description = processor.decode(outputs[0], skip_special_tokens=True)
    max_length = 250
    if len(description) > max_length:
        description = description[:max_length]
        if ' ' in description:
            description = description.rsplit(' ', 1)[0]
    return description

def process_images(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_folder, filename)
            alt_text = generate_alt_text(image_path)
            output_file = os.path.join(output_folder, f'{os.path.splitext(filename)[0]}.txt')
            with open(output_file, 'w') as f:
                f.write(alt_text)
            print(f'Generated alt text for {filename}: {alt_text}')

if __name__ == '__main__':
    input_folder = 'images'
    output_folder = 'output'
    process_images(input_folder, output_folder)


