# Diabetes Meal Planner

A Flask-based web application designed to support diabetes-aware meal planning through nutritional information and food recommendations.

## Overview

**Diabetes Meal Planner** is a web-based project that aims to make meal planning more informed and accessible for individuals managing diabetes.

The application considers a user's current blood sugar level and selected meal type to recommend suitable food options while taking into account carbohydrate content, protein requirements, and Glycemic Index (GI).

By bringing these nutritional factors together, the project demonstrates how web technologies can be used to support more informed food choices.

## Key Features

- **Blood Sugar-Based Planning:** Considers the user's current blood sugar level.
- **Meal-Type Selection:** Supports meal planning based on the selected meal type.
- **Nutritional Information:** Includes carbohydrate, calorie, and protein values.
- **Glycemic Index Classification:** Categorizes foods based on their GI values.
- **Food Recommendations:** Uses nutritional factors to support food selection.
- **Food Database:** Includes nutritional information for a variety of food items.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Flask | Backend web framework |
| HTML | Web page structure |
| Werkzeug | Flask-related web utilities |

## Project Structure

```text
Diabetes-Meal-Planner/
│
├── app.py
│
├── templates/
│   └── HTML templates
│
├── requirements.txt
│
└── README.md
```

## Installation & Setup

Follow these steps to run the project locally.

**1. Clone the repository**

```bash
git clone https://github.com/maharinmomota/Diabetes-Meal-Planner.git
```

**2. Navigate to the project directory**

```bash
cd Diabetes-Meal-Planner
```

**3. Create a virtual environment (optional)**

```bash
python -m venv venv
```

Activate it:

Windows:
```bash
venv\Scripts\activate
```

macOS/Linux:
```bash
source venv/bin/activate
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Run the Flask application**

```bash
flask --app app run --debug
```

**6. Open in your browser**

```text
http://127.0.0.1:5000
```

## Nutritional Parameters

The food database contains nutritional attributes such as:

- Carbohydrates (g)
- Calories (kcal)
- Protein (g)
- Serving size
- Glycemic Index (GI)
- GI classification (Low, Medium, High)

These parameters provide the nutritional basis for the meal-planning functionality.

## Learning Outcomes

Through this project, I explored:

- Building web applications using Python and Flask.
- Managing structured nutritional data.
- Working with food-related nutritional parameters.
- Applying conditional logic to recommendation-based applications.
- Understanding the integration of frontend templates with backend functionality.

## Future Improvements

- Personalized meal planning.
- Expanded nutritional database.
- Daily meal tracking.
- Weekly meal plan generation.
- Improved user interface and experience.
- More advanced nutritional recommendation logic.

## Disclaimer

This project is developed for educational and demonstration purposes. Its food recommendations are not a substitute for professional medical advice or individualized dietary guidance from a qualified healthcare professional.

## Author

**Maharin Islam Momota**

Computer Science & Engineering Student  
Bangladesh University of Professionals (BUP)

GitHub: [@maharinmomota](https://github.com/maharinmomota)

---

*Developed as a project exploring the application of web development and nutritional data in diabetes-aware meal planning.*
