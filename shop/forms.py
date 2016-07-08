from django import forms


class BookForm(forms.Form):
    name_field = forms.CharField(max_length=200, label='Search by name')
    # category_field = form.ChoiceField(get_categories())
