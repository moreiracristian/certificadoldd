from django import forms

class ExcelUploadForm(forms.Form):
    archivo = forms.FileField(label="Seleccionar archivo Excel")
