from django import forms


class FirstReservationForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Name", "class": "name-input"}),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "email-input"}),
    )
    person = forms.DecimalField(
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Person", "class": "person-input"}
        ),
    )
    timing = forms.TimeField(
        required=True,
        widget=forms.TimeInput(
            attrs={"placeholder": "Timing", "class": "timing-input"}
        ),
    )
    date = forms.DateField(
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "2025-03-19", "class": "date-input"}
        ),
    )


class SecondReservationForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Name"}),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
            }
        ),
    )
    phone = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Phone"}),
    )
    person = forms.DecimalField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Person"}),
    )
    timing = forms.TimeField(
        required=True,
        widget=forms.TimeInput(attrs={"placeholder": "Timing"}),
    )
    date = forms.DateField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "2025-03-19"}),
    )


class SubscribeMailingForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={"placeholder": "Email", "class": "subscribe-mailing-input"}
        ),
    )


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Name"}),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
            }
        ),
    )
    subject = forms.CharField(
        max_length=155,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Subject"}),
    )
    phone = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Phone"}),
    )
    message = forms.CharField(
        required=True, widget=forms.Textarea(attrs={"placeholder": "Message"})
    )
