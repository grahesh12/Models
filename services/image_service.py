
import os
import time
import torch
from datetime import datetime
from PIL import Image
from config import MODEL_PATHS, IMAGES_DIR, DEFAULT_GUIDANCE_SCALE, DEFAULT_INFERENCE_STEPS, IMAGE_SIZE
from core.model_loader import load_model, unload_model

class ImageService:
    def __init__(self):
        self.model_cache = {}

    def generate_image(self, prompt, style):
        start = time.time()

        # Select model path from config
        model_key = style if style in MODEL_PATHS else "dreamshaper"
        model_path = MODEL_PATHS[model_key]

        # Load model (from cache or fresh)
        if model_key not in self.model_cache:
            self.model_cache[model_key] = load_model(model_key)

        pipe = self.model_cache[model_key]
        pipe.to("cuda" if torch.cuda.is_available() else "cpu")

        # Run generation
        result = pipe(
            prompt,
            guidance_scale=DEFAULT_GUIDANCE_SCALE,
            num_inference_steps=DEFAULT_INFERENCE_STEPS,
            height=IMAGE_SIZE,
            width=IMAGE_SIZE
        )

        if not result.images:
            return {"success": False, "error": "No image generated"}

        # Save the image
        image = result.images[0]
        filename = f"{int(time.time())}_{style}.png"
        filepath = os.path.join(IMAGES_DIR, filename)
        os.makedirs(IMAGES_DIR, exist_ok=True)
        image.save(filepath)

        end = time.time()

        return {
            "success": True,
            "filename": filename,
            "style": style,
            "generation_time": round(end - start, 2)
        }
