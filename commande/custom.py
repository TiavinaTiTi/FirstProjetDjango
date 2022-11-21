from django.forms.widgets import TextInput


class Custom(TextInput):
    input_type = "text"
    template_name = "base/text.html"