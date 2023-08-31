from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb

class TrainModel:
    def __init__(self, X, y, test_size=0.3, random_state=42):
        self.X = X
        self.y = y
        self.test_size = test_size
        self.random_state = random_state

    def _prepare_data(self):
        X_train, X_val, y_train, y_val = train_test_split(self.X, self.y, test_size=self.test_size, random_state=self.random_state, stratify=self.y)
        smote = SMOTE(random_state=self.random_state)
        X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)
        return X_train_smote, y_train_smote, X_val, y_val

    def train_random_forest(self):
        X_train, X_val, y_train, y_val = train_test_split(self.X, self.y, test_size=0.3, random_state=42, stratify=self.y)
        smote = SMOTE(random_state=42)
        X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)
        model = RandomForestClassifier(random_state=42, class_weight='balanced')
        model.fit(X_train_smote, y_train_smote)
        return model, X_val, y_val


    def train_xgboost(self, n_estimators=100):
        X_train_smote, y_train_smote, X_val, y_val = self._prepare_data()
        model = xgb.XGBClassifier(n_estimators=n_estimators, random_state=self.random_state)
        model.fit(X_train_smote, y_train_smote)
        return model, X_val, y_val

