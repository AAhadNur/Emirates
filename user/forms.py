from django import forms
from user.models import CustomUser


# Form for creating Normal User ( Passenger and Employee )
class CreateNormalUserForm(forms.ModelForm):

    PASSENGER = 'Passenger'
    EMPLOYEE = 'Employee'
    MANAGEMENT = 'Management'
    MALE = 'Male'
    FEMALE = 'Female'
    OTHERS = 'Others'

    USER_TYPE_CHOICES = (
        (PASSENGER, 'Passenger'),
        (EMPLOYEE, 'Employee'),
        (MANAGEMENT, 'Management'),
    )

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Others'),
    )

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, widget=forms.RadioSelect)
    user_type = forms.ChoiceField(
        choices=USER_TYPE_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone', 'date_of_birth',
                  'gender', 'nationality', 'national_id', 'user_type']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


# Form for creating Management User
class CreateSuperUserForm(forms.ModelForm):

    PASSENGER = 'Passenger'
    EMPLOYEE = 'Employee'
    MANAGEMENT = 'Management'
    MALE = 'Male'
    FEMALE = 'Female'
    OTHERS = 'Others'

    USER_TYPE_CHOICES = (
        (PASSENGER, 'Passenger'),
        (EMPLOYEE, 'Employee'),
        (MANAGEMENT, 'Management'),
    )

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Others'),
    )

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, widget=forms.RadioSelect)
    user_type = forms.ChoiceField(
        choices=USER_TYPE_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone', 'date_of_birth',
                  'gender', 'nationality', 'national_id', 'is_staff', 'is_superuser', 'date_joined', 'user_type']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
