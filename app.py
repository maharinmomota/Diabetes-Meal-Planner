from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample food database with nutritional information
# Each food has: name, carbs (grams), calories, protein (grams), serving size, glycemic_index
# Glycemic Index (GI): Low (<55), Medium (56-69), High (>70)
FOOD_DATABASE = [
    {"id": 1, "name": "Oatmeal", "carbs": 27, "calories": 150, "protein": 5, "serving": "1 cup", "gi": 55, "gi_category": "Low"},
    {"id": 2, "name": "Brown Rice", "carbs": 45, "calories": 215, "protein": 5, "serving": "1 cup", "gi": 68, "gi_category": "Medium"},
    {"id": 3, "name": "Chicken Breast", "carbs": 0, "calories": 165, "protein": 31, "serving": "100g", "gi": 0, "gi_category": "None"},
    {"id": 4, "name": "Salmon", "carbs": 0, "calories": 206, "protein": 22, "serving": "100g", "gi": 0, "gi_category": "None"},
    {"id": 5, "name": "Broccoli", "carbs": 6, "calories": 31, "protein": 3, "serving": "1 cup", "gi": 15, "gi_category": "Low"},
    {"id": 6, "name": "Apple", "carbs": 25, "calories": 95, "protein": 0, "serving": "1 medium", "gi": 36, "gi_category": "Low"},
    {"id": 7, "name": "Sweet Potato", "carbs": 27, "calories": 112, "protein": 2, "serving": "1 medium", "gi": 63, "gi_category": "Medium"},
    {"id": 8, "name": "Quinoa", "carbs": 39, "calories": 222, "protein": 8, "serving": "1 cup", "gi": 53, "gi_category": "Low"},
    {"id": 9, "name": "Greek Yogurt", "carbs": 9, "calories": 100, "protein": 17, "serving": "170g", "gi": 11, "gi_category": "Low"},
    {"id": 10, "name": "Almonds", "carbs": 6, "calories": 164, "protein": 6, "serving": "28g", "gi": 0, "gi_category": "None"},
    {"id": 11, "name": "Spinach", "carbs": 1, "calories": 7, "protein": 1, "serving": "1 cup", "gi": 15, "gi_category": "Low"},
    {"id": 12, "name": "Whole Wheat Bread", "carbs": 12, "calories": 69, "protein": 4, "serving": "1 slice", "gi": 74, "gi_category": "High"},
    {"id": 13, "name": "Eggs", "carbs": 1, "calories": 78, "protein": 6, "serving": "1 large", "gi": 0, "gi_category": "None"},
    {"id": 14, "name": "Lentils", "carbs": 40, "calories": 230, "protein": 18, "serving": "1 cup", "gi": 32, "gi_category": "Low"},
    {"id": 15, "name": "Avocado", "carbs": 12, "calories": 234, "protein": 3, "serving": "1 medium", "gi": 15, "gi_category": "Low"},
    {"id": 16, "name": "White Rice", "carbs": 53, "calories": 242, "protein": 4, "serving": "1 cup", "gi": 73, "gi_category": "High"},
    {"id": 17, "name": "Beans (Black)", "carbs": 41, "calories": 227, "protein": 15, "serving": "1 cup", "gi": 30, "gi_category": "Low"},
    {"id": 18, "name": "Cottage Cheese", "carbs": 6, "calories": 163, "protein": 28, "serving": "1 cup", "gi": 10, "gi_category": "Low"},
    {"id": 19, "name": "Tomato", "carbs": 7, "calories": 32, "protein": 2, "serving": "1 medium", "gi": 15, "gi_category": "Low"},
    {"id": 20, "name": "Cucumber", "carbs": 4, "calories": 16, "protein": 1, "serving": "1 cup", "gi": 15, "gi_category": "Low"},
]
