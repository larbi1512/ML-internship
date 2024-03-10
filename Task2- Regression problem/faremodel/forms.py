from django import forms

class FarePredictionForm(forms.Form):
    Car_Condition = forms.IntegerField(label='Car Condition', min_value=0, max_value=2)
    Traffic_Condition = forms.IntegerField(label='Traffic Condition', min_value=0, max_value=2)
    pasenger_count = forms.IntegerField(label='pasenger_count', min_value=0, max_value=6)
    distance = forms.FloatField(label='distance' , min_value=0)
    year = forms.IntegerField(label='year', min_value=2009, max_value=2024)
    Weather = forms.IntegerField(label='Weather', min_value=0)
    bearing = forms.FloatField(label='bearing', min_value=0, max_value=360)
    month = forms.IntegerField(label='month', min_value=1, max_value=12)
    weekday = forms.IntegerField(label='weekday', min_value=0, max_value=6)
    hour = forms.IntegerField(label='hour', min_value=0, max_value=23)

    