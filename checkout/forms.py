from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """

        # call the init method to set the form up as it would be by default
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }
        # Sets auto focus to to the full name box first
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                # add star if field required
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            # placeholder names to values in dictionary above
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # add css style
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # turn off lables as we are using placeholders
            self.fields[field].label = False
