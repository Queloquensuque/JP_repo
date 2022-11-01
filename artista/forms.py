from django import forms

class ArtistForm(forms.Form):
    name = forms.CharField(
        label="Nombre del artista",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "artist-name",
                "placeholder": "Nombre del artista",
                "required": "True",
            }
        )
    )
    anio= forms.IntegerField(
        label="anio:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "artista-anio",
                "placeholder": "Año de inicio del artista",
                "required": "True",
                }
        ),
    )