from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser



class CustomUserCreationForm(UserCreationForm): #this is stupid, you are stupid Corbin
    class Meta:
        model = CustomUser
        fields = ('email','first_name','last_name')

