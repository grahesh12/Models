from pathlib import Path
import torch
from diffusers import StableDiffusionPipeline
from config import MODEL_PATHS
import gc

def load_model(model_key):
    # Convert Windows-style path to HF-compatible POSIX path
    model_path = Path(MODEL_PATHS[model_key]).as_posix()

    device = "cuda" if torch.cuda.is_available() else "cpu"

    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()

    pipe = StableDiffusionPipeline.from_pretrained(
        model_path,
        torch_dtype=torch.float16 if device == "cuda" else torch.float32,
        safety_checker=None,
        requires_safety_checker=False
    )

    pipe = pipe.to(device)
    return pipe


# Cleanly unload model from memory

def unload_model(pipe):
    try:
        if pipe is not None:
            pipe.to("cpu")  # Move to CPU first
            del pipe        # Delete pipeline
            gc.collect()    # Python garbage collection
            if torch.cuda.is_available():
                torch.cuda.empty_cache()  # Clear GPU cache
    except Exception as e:
        print(f"Error during model unload: {e}")
