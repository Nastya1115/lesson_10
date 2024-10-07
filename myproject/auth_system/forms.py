from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from auth_system.models import User

class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

class UserAuthForm(AuthenticationForm):
    class Meta:
        model = User