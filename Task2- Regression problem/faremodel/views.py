import os
import joblib
import numpy as np
from django.shortcuts import render
from .forms import FarePredictionForm


def predict_fare(request):
    if request.method == 'POST':
        form = FarePredictionForm(request.POST)
        if form.is_valid():
            # load the model 
            model = joblib.load(os.path.join(os.path.dirname(__file__), 'models', 'best_xgb_regressor.pkl'))
            
            # Extract input data from the form
            new_data = np.array(list(form.cleaned_data.values())).reshape(1, -1)
            
            # Perform prediction
            predicted_fare = model.predict(new_data)[0]
            
            # Prepare the response
            context = {
                'form': form,
                'predicted_fare': predicted_fare,
            }
            return render(request, 'index.html', context)
    else:
        form = FarePredictionForm()

    context = {'form': form}
    return render(request, 'index.html', context)
