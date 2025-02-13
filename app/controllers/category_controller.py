from flask import Blueprint, jsonify
from app.models.models import Category

category_bp = Blueprint('category', __name__)

@category_bp.route('/categories', methods=['GET'])
def get_all_categories():
    categories = Category.query.all()
    if not categories:
        return jsonify({"message": "No categories found"}), 404

    categories_list = [category.to_dict() for category in categories]
    return jsonify({"message": "Categories fetched successfully", "categories": categories_list}), 200


@category_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify(status='OK', service='user-read'), 200


