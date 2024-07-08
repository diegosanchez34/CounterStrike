import joblib
import os
import numpy as np

# Ruta base de los modelos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELOS_DIR = os.path.join(BASE_DIR, 'CS', 'modelos')

# Cargar el scaler y los modelos
scaler = joblib.load(os.path.join(MODELOS_DIR, 'scaler.pkl'))
logreg = joblib.load(os.path.join(MODELOS_DIR, 'logreg.pkl'))
tree_clf = joblib.load(os.path.join(MODELOS_DIR, 'tree_clf.pkl'))
rf_clf = joblib.load(os.path.join(MODELOS_DIR, 'rf_clf_model_compressed.pkl.gz'))
meta_clf = joblib.load(os.path.join(MODELOS_DIR, 'meta_clf.pkl'))

def predict(new_data):
    # Normalizar los nuevos datos
    new_data_scaled = scaler.transform(new_data)

    # Hacer predicciones con los modelos base
    logreg_pred = logreg.predict_proba(new_data_scaled)[:, 1]
    tree_pred = tree_clf.predict_proba(new_data_scaled)[:, 1]
    rf_pred = rf_clf.predict_proba(new_data_scaled)[:, 1]

    # Combinar las predicciones de los modelos base para el modelo de stacking
    stacking_features = np.concatenate((new_data_scaled, logreg_pred.reshape(-1, 1), tree_pred.reshape(-1, 1), rf_pred.reshape(-1, 1)), axis=1)

    # Hacer predicciones utilizando el modelo de stacking
    stacking_pred = meta_clf.predict(stacking_features)
    stacking_pred_proba = meta_clf.predict_proba(stacking_features)[:, 1]

    return stacking_pred, stacking_pred_proba

scalerRF = joblib.load(os.path.join(MODELOS_DIR, 'scalerRF.pkl'))
rfc = joblib.load(os.path.join(MODELOS_DIR, 'rfc_model_compressed.pkl.gz'))

def predictRF(new_data):
    # Normalizar los nuevos datos
    new_data_scaled = scalerRF.transform(new_data)

    # Hacer predicciones con el modelo de Random Forest
    rfc_pred = rfc.predict(new_data_scaled)
    rfc_pred_proba = rfc.predict_proba(new_data_scaled)[:, 1]

    return rfc_pred, rfc_pred_proba
