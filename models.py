from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

def train_models(X_train, y_train):
    models = {
        "Naive Bayes": MultinomialNB(),
        "SVM": LinearSVC(),
        "Random Forest": RandomForestClassifier(n_estimators=300, random_state=42),
        "Logistic Regression": LogisticRegression(max_iter=500)
    }
    for name, model in models.items():
        model.fit(X_train, y_train)
        print(f"{name} trained.")
    return models
