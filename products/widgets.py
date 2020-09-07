from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


# Code from here:
# https://github.com/django/django/blob/master/django/forms/widgets.py
class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    # change location template is loaded from
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'
