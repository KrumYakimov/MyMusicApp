from django import forms


class AlbumFormPlaceholderMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        # Setting the placeholders for each field
        form.fields["album_name"].widget = forms.TextInput(
            attrs={"placeholder": "Album Name"}
        )

        form.fields["artist"].widget = forms.TextInput(
            attrs={"placeholder": "Artist"}
        )

        form.fields["description"].widget = forms.Textarea(
            attrs={"placeholder": "Description"}
        )

        form.fields["image_url"].widget = forms.URLInput(
            attrs={"placeholder": "Image URL"}
        )

        form.fields["price"].widget = forms.NumberInput(
            attrs={"placeholder": "Price", "step": 0.01}
        )

        return form
