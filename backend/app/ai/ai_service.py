import ast
import os

class AIService:
    def __init__(self):
        self.model = None

    def parse_code(self, code):
        try:
            tree = ast.parse(code)
            return tree
        except Exception as e:
            return str(e)

    def extract_features(self, tree):
        if isinstance(tree, str):
            return {"error": tree}
            
        features = {
            "num_loops": 0,
            "num_functions": 0,
            "num_classes": 0,
            "has_docstrings": 0,
        }

        for node in ast.walk(tree):
            if isinstance(node, (ast.For, ast.While)):
                features["num_loops"] += 1
            if isinstance(node, ast.FunctionDef):
                features["num_functions"] += 1
                if ast.get_docstring(node):
                    features["has_docstrings"] += 1
            if isinstance(node, ast.ClassDef):
                features["num_classes"] += 1

        return features

    def get_educational_feedback(self, features):
        suggestions = []
        explanation = "This code structure suggests "
        
        if features["num_loops"] > 2:
            suggestions.append("High complexity detected: Consider using vectorized operations or built-in functions to reduce nested loops.")
        
        if features["num_functions"] == 0:
            suggestions.append("Modularization Tip: Try wrapping your logic in functions to make it reusable and easier to test.")
        
        if features["has_docstrings"] < features["num_functions"]:
            suggestions.append("Best Practice: Add docstrings to your functions to explain what they do. This is crucial for collaborative ASEAN projects.")

        if not suggestions:
            suggestions.append("Excellent structure! Your code follows clean coding principles.")

        return {
            "explanation": explanation + (f"a modular design with {features['num_functions']} functional blocks." if features['num_functions'] > 0 else "a script-based approach."),
            "suggestions": suggestions
        }

    def analyze(self, code):
        tree = self.parse_code(code)
        if isinstance(tree, str):
            return {
                "error": True,
                "message": f"Syntax Error: {tree}",
                "suggestion": "Check your code for missing colons or indentation errors."
            }

        features = self.extract_features(tree)
        feedback = self.get_educational_feedback(features)

        # AI Prediction logic (Simplified for demo, can be expanded with ML)
        complexity_score = (features["num_loops"] * 30) + (features["num_functions"] * 10)
        level = "Beginner" if complexity_score < 40 else "Intermediate" if complexity_score < 100 else "Advanced"

        return {
            "features": features,
            "prediction": {
                "level": level,
                "explanation": feedback["explanation"],
                "suggestions": feedback["suggestions"]
            }
        }
