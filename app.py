from flask import Flask
from routes.image_routes import create_image_routes
from services.image_service import ImageService

# Create the Flask application instance
app = Flask(__name__)

# Initialize the image generation service (handles model loading and image creation)
image_service = ImageService()

# Register the blueprint that contains the image generation routes
app.register_blueprint(create_image_routes(image_service))

# Entry point for running the app locally
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000,debug=True)
