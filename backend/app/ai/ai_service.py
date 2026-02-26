import ast
import joblib
import os

class AIService:
    def __init__(self):
        self.model = None
        # Placeholder for model loading
        # if os.path.exists("model.pkl"):
        #     self.model = joblib.load("model.pkl")

    def parse_code(self, code):
        try:
            tree = ast.parse(code)
            return tree
        except Exception as e:
            return None

    def extract_features(self, tree):
        if tree is None:
            return [0, 0]
            
        features = {
            "num_loops": 0,
            "num_functions": 0,
        }

        for node in ast.walk(tree):
            if isinstance(node, ast.For) or isinstance(node, ast.While):
                features["num_loops"] += 1
            if isinstance(node, ast.FunctionDef):
                features["num_functions"] += 1

        return list(features.values())

    def analyze(self, code):
        tree = self.parse_code(code)
        features = self.extract_features(tree)
        
        # Simple rule-based logic if model isn't trained yet
        complexity = "Low"
        if features[0] > 2:
            complexity = "High"
        elif features[0] > 0:
            complexity = "Medium"

        return {
            "features": {
                "num_loops": features[0],
                "num_functions": features[1]
            },
            "prediction": {
                "complexity": complexity,
                "suggestion": "Consider splitting functions" if features[1] > 5 else "Code looks clean"
            }
        }
