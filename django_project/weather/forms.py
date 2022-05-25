from django import forms

from django_project.weather.models import City
from django_project.weather.views import get_request_weather_data


class CreateCityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ('name', )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',  'placeholder': ' 都市', 'label': 'city'}),
        }

    def clean_name(self):
        value = self.cleaned_data['name']

        r = get_request_weather_data(value)
        has_error = 'error' in r.text[:10]
        if has_error:
            raise forms.ValidationError(
                '存在しない都市名です'
            )
        # responseからcityを取り出す
        value = r.json()['location']['name']
        return value
