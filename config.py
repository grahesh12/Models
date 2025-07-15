import os

# Base directory for relative paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Directory where generated images will be saved
IMAGES_DIR = os.path.join(BASE_DIR, "static", "images")

# Updated model paths based on correct user directory
MODEL_PATHS = {
    "dreamshaper": os.path.join(BASE_DIR, "model", "dreamshaper_model"),
    "realistic_vision": os.path.join(BASE_DIR, "model", "realistic_vision_model"),
}

# Image generation parameters
IMAGE_SIZE = 512                      # Default width/height
DEFAULT_GUIDANCE_SCALE = 7.5         # How strongly the model sticks to the prompt
DEFAULT_INFERENCE_STEPS = 25         # Number of denoising steps
MODEL_TIMEOUT = 600                  # Time after which unused models are unloaded (in seconds)
MAX_MODELS_IN_MEMORY = 1             # LRU cache limit for loaded models
MAX_IMAGES_TO_KEEP = 100             # Cleanup threshold for saved images

# Keyword scoring used for auto-selecting model style
DREAMSHAPER_KEYWORDS = {"anime": 2, "illustration": 2, "fantasy": 2}
REALISTIC_KEYWORDS = {"realistic": 2, "photograph": 2, "photo": 2}
