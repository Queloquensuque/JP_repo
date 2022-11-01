from django import forms

class BandaForm(forms.Form):
    name = forms.CharField(
        label="Nombre de la banda",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "banda-name",
                "placeholder": "Nombre de la banda",
                "required": "True",
            }
        )
    )
    anio= forms.IntegerField(
        label="Año:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "banda-anio",
                "placeholder": "Año de inicio",
                "required": "True",
                }
        ),
    )