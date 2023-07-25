from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm as Auth, PasswordResetForm
from django.core.exceptions import ValidationError
from django.template import loader
from django.core.mail import EmailMultiAlternatives

from users.models import User
from users.utils import send_email_for_verify


# class StyleFormMixin:
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'


class AuthenticationForm(Auth):
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(
                self.request,
                username=username,
                password=password,
            )
            # if not self.user_cache.email_verify:
            #     send_email_for_verify(self.request, self.user_cache)
            #     raise ValidationError(
            #         'Email not verify, check your email',
            #         code='invalid_login',
            #     )

            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                if not self.user_cache.email_verify:
                    send_email_for_verify(self.request, self.user_cache)
                    raise ValidationError(
                        'Email not verify, check your email',
                        code='invalid_login',
                    )
                else:
                    self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


class UserRecoveryForm(PasswordResetForm):  # StyleFormMixin,
    email = forms.EmailField(max_length=100)

    def send_mail(
            self,
            subject_template_name,
            email_template_name,
            context,
            from_email,
            to_email,
            html_email_template_name=None,
    ):
        """
        Send a django.core.mail.EmailMultiAlternatives to `to_email`.
        """
        subject = loader.render_to_string(subject_template_name, context)
        # Email subject *must not* contain newlines
        subject = "".join(subject.splitlines())
        body = loader.render_to_string(email_template_name, context)

        email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
        if html_email_template_name is not None:
            html_email = loader.render_to_string(html_email_template_name, context)
            email_message.attach_alternative(html_email, "text/html")

        email_message.send()
        print(body)
        print(context)

