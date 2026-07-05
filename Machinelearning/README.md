# 🤖 Machine Learning

Small classification projects using `scikit-learn`, demonstrating different ML algorithms trained and evaluated on a dataset.

## Projects

| File | Algorithm | Description |
|---|---|---|
| [`Decisiontree.py`]('./Decisiontree.py') | Decision Tree Classifier | Trains a decision tree model and evaluates it with accuracy score and classification report. |
| `KNN.py` | K-Nearest Neighbors | Trains a KNN classifier and evaluates prediction performance. |
| `Naivebayes.py` | Gaussian Naive Bayes | Trains a Naive Bayes classifier for classification tasks. |
| `Randomforest.py` | Random Forest Classifier | Trains an ensemble random forest model and evaluates it. |

## Common Workflow
Each script generally follows the same pattern:
1. Load data with `pandas`
2. Split into train/test sets with `train_test_split`
3. Train the respective model
4. Evaluate using `accuracy_score` and `classification_report`

## Requirements
```bash
pip install pandas numpy scikit-learn
```

## Notes
- Make sure the dataset path/CSV referenced in each script is available before running.
- These are meant as learning references for comparing classic ML algorithms side by side.
