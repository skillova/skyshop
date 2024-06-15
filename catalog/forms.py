from django.forms import ModelForm, forms, BooleanField

from catalog.models import Product, Version

words = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class StyleFormMixin(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
                field.widget.attrs["placeholder"] = field.label
            else:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ("owner",)

    def clean_name(self):
        cleaned_data = self.cleaned_data.get("name")

        if cleaned_data in words:
            raise forms.ValidationError("Невалидное наименование")
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get("description")

        if cleaned_data in words:
            raise forms.ValidationError("Невалидное описание")
        return cleaned_data


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
