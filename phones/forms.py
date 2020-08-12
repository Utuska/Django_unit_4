from django import forms

class PhonesFilterForm(forms.Form):
    ordering = forms.ChoiceField(label="сортировка", required=False,
                                 choices=[["name", "по алфавиту"],
                                          ["price", "дешевые сверху"],
                                          ["-price", "дорогие сверху"]
                                          ]
                                 )