# Task 07 — Machine Learning Foundations

Train/Test Split, Overfitting/Underfitting, Bias-Variance Tradeoff, and Linear Regression, implemented with scikit-learn on the Titanic dataset.

## Contents
- `Task07_ML_Foundations.ipynb` — full notebook (theory + code + plots)
- `titanic.csv` — dataset used (loaded via seaborn's built-in Titanic copy)
- `env_screenshot.png` — Python environment showing installed packages
- `metrics_screenshot.png` — trained Linear Regression model's evaluation metrics
- `bias_variance_plot.png` — training vs. test error across polynomial degrees
- `predicted_vs_actual.png` — predicted vs. actual fare scatter plot
- `learning_curve.png` — learning curve (training size vs. R² score)

## Environment
- Python 3
- scikit-learn, pandas, numpy, matplotlib, seaborn
- Developed on Windows using WSL2 (Ubuntu)

## Setup
```bash
pip install scikit-learn pandas numpy matplotlib seaborn jupyter
jupyter notebook Task07_ML_Foundations.ipynb
```

## Summary
- **Part A:** Train/test split theory, `train_test_split` implementation, role of `random_state`, validation vs. test sets.
- **Part B:** Overfitting/underfitting definitions, bias-variance tradeoff, techniques to reduce overfitting, polynomial-degree error plot.
- **Part C:** Linear regression theory (normal equation vs. gradient descent), model trained on Titanic data to predict `fare`, evaluated with MSE/RMSE/R².
- **Part D:** Data cleaning + encoding, reusable `load_data()` / `split_data()` / `train_model()` / `evaluate_model()` functions, comparison across 60/40, 80/20, 90/10 splits, 5-fold cross-validation, learning curve.
- **Bonus:** Polynomial regression (degree 2 and 3) compared against the plain linear model.

## Results (Linear Regression, 80/20 split, predicting fare)
| Metric | Value |
|---|---|
| MSE | ~928.6 |
| RMSE | ~30.5 |
| R² | ~0.40 |

Fare prediction has inherent noise (ticket pricing depended on factors like exact cabin/deck not present in this feature set), so this R² is a reasonable result for the features used.
