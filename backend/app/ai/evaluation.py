from sklearn.metrics import classification_report, accuracy_score

def evaluate_model(model, X_test, y_test):
    """
    Evaluates the ML model and returns a report.
    This is crucial for hackathon technical points.
    """
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred, output_dict=True)
    accuracy = accuracy_score(y_test, y_pred)
    
    return {
        "accuracy": accuracy,
        "report": report
    }
