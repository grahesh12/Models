
from flask import Blueprint, request, jsonify

# Define a route generator function that accepts the image_service instance
def create_image_routes(image_service):
    image_bp = Blueprint('image_routes', __name__)

    @image_bp.route("/api/generate", methods=["POST"])
    def generate():
        # Parse JSON input
        data = request.get_json()
        prompt = data.get("prompt", "").strip()
        style = data.get("artStyle", "dreamshaper")

        # Validate input
        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        # Generate the image using the requested or detected model style
        result = image_service.generate_image(prompt, style)

        if result["success"]:
            return jsonify({
                "status": "success",
                "image_url": f"/images/{result['filename']}",
                "filename": result["filename"],
                "style_used": result["style"],
                "generation_time": result["generation_time"]
            }), 200
        else:
            return jsonify({"status": "error", "message": result["error"]}), 500

    return image_bp
