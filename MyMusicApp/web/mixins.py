from django import forms


class ProfileFormPlaceholderMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        form.fields['username'].widget = forms.TextInput(
            attrs={'placeholder': 'Username'}
        )

        form.fields["email"].widget = forms.EmailInput(
            attrs={"placeholder": "Email"}
        )

        form.fields["age"].widget = forms.NumberInput(
            attrs={"placeholder": "Age"}
        )

        return form


