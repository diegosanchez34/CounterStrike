from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .forms import PredictionForm, PredictionRFForm
from .ml_model import predict, predictRF, logreg, tree_clf, rf_clf, scaler, meta_clf, scalerRF, rfc
import pandas as pd
import numpy as np

@csrf_exempt
def index(request):
    prediction = None
    prediction_proba = None
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_data = pd.DataFrame([data])

            expected_features = [
                'InternalTeamId', 'MatchId', 'RoundId', 'PrimaryAssaultRifle', 'PrimarySniperRifle', 'PrimaryPistol',
                'RoundKills', 'RoundHeadshots', 'RoundFlankKills', 'RoundStartingEquipmentValue', 'TeamStartingEquipmentValue',
                'MatchKills', 'MatchAssists'
            ]
            
            for feature in expected_features:
                if feature not in new_data.columns:
                    new_data[feature] = 0
            
            new_data = new_data[expected_features]

            new_data_scaled = scaler.transform(new_data)

            logreg_pred = logreg.predict_proba(new_data_scaled)[:, 1]
            tree_pred = tree_clf.predict_proba(new_data_scaled)[:, 1]
            rf_pred = rf_clf.predict_proba(new_data_scaled)[:, 1]

            stacking_features = np.concatenate((new_data_scaled, logreg_pred.reshape(-1, 1), tree_pred.reshape(-1, 1), rf_pred.reshape(-1, 1)), axis=1)

            prediction = meta_clf.predict(stacking_features)[0]
            probabilidad = meta_clf.predict_proba(stacking_features)[:, 1][0]
            prediction_proba = round(probabilidad*100, 2)
            
    else:
        form = PredictionForm()

    return render(request, 'index.html', {
        'form': form,
        'prediction': prediction,
        'prediction_proba': prediction_proba
    })

@csrf_exempt
def randomforest(request):
    prediction = None
    prediction_proba = None

    if request.method == 'POST':
        form = PredictionRFForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_data = pd.DataFrame([data])

            # Normalizar los nuevos datos
            new_data_scaled = scalerRF.transform(new_data)

            # Hacer predicciones utilizando el modelo RFC
            rf_pred = rfc.predict(new_data_scaled)
            rf_pred_proba = rfc.predict_proba(new_data_scaled)[:, 1]

            prediction = rf_pred[0]
            probabilidad = rf_pred_proba[0]
            prediction_proba = round(probabilidad*100, 2)
    else:
        form = PredictionRFForm()

    return render(request, 'randomforest.html', {
        'form': form,
        'prediction': prediction,
        'probability': prediction_proba,
    })


@csrf_exempt
def predict_view(request):
    prediction = None
    prediction_proba = None
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_data = pd.DataFrame([data])

            expected_features = [
                'InternalTeamId', 'MatchId', 'RoundId', 'PrimaryAssaultRifle', 'PrimarySniperRifle', 'PrimaryPistol',
                'RoundKills', 'RoundHeadshots', 'RoundFlankKills', 'RoundStartingEquipmentValue', 'TeamStartingEquipmentValue',
                'MatchKills', 'MatchAssists'
            ]
            
            for feature in expected_features:
                if feature not in new_data.columns:
                    new_data[feature] = 0
            
            new_data = new_data[expected_features]

            new_data_scaled = scaler.transform(new_data)

            logreg_pred = logreg.predict_proba(new_data_scaled)[:, 1]
            tree_pred = tree_clf.predict_proba(new_data_scaled)[:, 1]
            rf_pred = rf_clf.predict_proba(new_data_scaled)[:, 1]

            stacking_features = np.concatenate((new_data_scaled, logreg_pred.reshape(-1, 1), tree_pred.reshape(-1, 1), rf_pred.reshape(-1, 1)), axis=1)

            prediction = meta_clf.predict(stacking_features)[0]
            prediction_proba = meta_clf.predict_proba(stacking_features)[:, 1][0]
            
    else:
        form = PredictionForm()

    return render(request, 'CS/predict.html', {
        'form': form,
        'prediction': prediction,
        'prediction_proba': prediction_proba
    })


@csrf_exempt
def predictRF_view(request):
    prediction = None
    prediction_proba = None

    if request.method == 'POST':
        form = PredictionRFForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_data = pd.DataFrame([data])

            # Normalizar los nuevos datos
            new_data_scaled = scalerRF.transform(new_data)

            # Hacer predicciones utilizando el modelo RFC
            rf_pred = rfc.predict(new_data_scaled)
            rf_pred_proba = rfc.predict_proba(new_data_scaled)[:, 1]

            prediction = rf_pred[0]
            prediction_proba = rf_pred_proba[0]
    else:
        form = PredictionRFForm()

    return render(request, 'CS/predictRF.html', {
        'form': form,
        'prediction': prediction,
        'probability': prediction_proba,
    })