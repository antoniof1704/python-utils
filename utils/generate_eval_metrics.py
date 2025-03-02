
from matplotlib import pyplot as plt

from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    f1_score,
    recall_score,
    precision_score,
)

# Create a function that will automatically provide the eval metrics spcified below for a model

def generate_eval_metrics(actual, predicted):
    
    # Confusion Matrix

    cm_result  = confusion_matrix(actual, predicted)

    print("Confusion Matrix: ")
    print(cm_result)

    # Accuracy
    accuracy = accuracy_score(actual, predicted)
    print(f"Accuracy: {accuracy * 100:.2f}%")

    # Precision
    precision = precision_score(actual, predicted)
    print(f"Precision: {precision:.2f}")

    # Recall
    recall = recall_score(actual, predicted)
    print(f"Recall: {recall:.2f}")

    # F1 Score
    f1 = f1_score(actual, predicted)
    print(f"F1 Score: {f1:.2f}")