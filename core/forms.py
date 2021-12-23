from .models import *

class VehicleUseForm(forms.ModelForms):
    class Meta:
    model = VehicleUse
    fields = ['__all__']
