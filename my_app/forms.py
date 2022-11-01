from django import forms

class CountryForm(forms.Form):
    name = forms.CharField(
        label="Nombre del país",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "country-name",
                "placeholder": "Nombre del país",
                "required": "True",
            }
        )
    )
    capital= forms.CharField(
        label="Capital:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "country-capital",
                "placeholder": "Nombre de la capital",
                "required": "True",
                }
        ),
    )