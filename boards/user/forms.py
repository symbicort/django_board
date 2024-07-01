from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User = get_user_model()

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

class LoginForm(AuthenticationForm):
    class Meta(AuthenticationForm.Meta):
        model = User
