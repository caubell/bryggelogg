from django import forms
from Bryggelogg.models import Bryggelogg
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class BryggeloggForm(forms.ModelForm):
    """
    def _meskevann(self):
        return (self.malt_1 + self.malt_2 + self.malt_3 + self.malt_4 + self.malt_5) * 3

    total = property(_meskevann)
    """
    class Meta():
        model = Bryggelogg
        labels = {'malt_1': 'Malt', 'malt_2': '', 'malt_3': '', 'malt_4': '', 'malt_5': '',
         'm_mengde_1': 'Mengde', 'm_mengde_2': '', 'm_mengde_3': '', 'm_mengde_4': '', 'm_mengde_5': ''
         ,'humle_1': 'Humle','humle_2': '','humle_3': '','humle_4': '','humle_5': '',
         'h_mengde_1': 'Mengde','h_mengde_2': '','h_mengde_2': '','h_mengde_3': '','h_mengde_4': '','h_mengde_5': '',
         'fg': '', 'og': '', 'abv': '', 'bryggnr': '', 'dato': '', 'navn': '', 'effektivitet': '',
         'sluttvolum': '', 'utbytte': '', 'mesketemperatur': '', 'rating': '', 'meskevann': '', 'kokevolum': '',
         'etterfylling': '', 'gjaer': ''}
        fields = '__all__'
        widgets = {
            'bryggnr': forms.TextInput(attrs={'placeholder': 'Bryggnr.'}),
            'navn': forms.TextInput(attrs={'placeholder': 'Navn'}),
            'fg': forms.TextInput(attrs={'placeholder': 'FG'}),
            'og': forms.TextInput(attrs={'placeholder': 'OG'}),
            'abv': forms.TextInput(attrs={'placeholder': 'ABV'}),
            'effektivitet': forms.TextInput(attrs={'placeholder': 'Effektivitet'}),
            'sluttvolum': forms.TextInput(attrs={'placeholder': 'Sluttvolum'}),
            'utbytte': forms.TextInput(attrs={'placeholder': 'Utbytte'}),
            'mesketemperatur': forms.TextInput(attrs={'placeholder': 'Mesketemperatur'}),
            'rating': forms.TextInput(attrs={'placeholder': 'Rating'}),
            'meskevann': forms.TextInput(attrs={'placeholder': 'Meskevann'}),
            'kokevolum': forms.TextInput(attrs={'placeholder': 'Kokevolum'}),
            'etterfylling': forms.TextInput(attrs={'placeholder': 'Etterfylling'}),
            'gjaer': forms.TextInput(attrs={'placeholder': 'Gjær'}),
            'dato': forms.TextInput(attrs={'placeholder': 'Dato'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('bryggnr', css_class='form-group col-md-3'),
                Column('dato', css_class='form-group col-md-3'),
                Column('navn', css_class='form-group col-md-6'),
                css_class='form-row'
                ),
            Row(
                Column('og', css_class='form-group col-md-2'),
                Column('fg', css_class='form-group col-md-2'),
                Column('abv', css_class='form-group col-md-2'),
                Column('effektivitet', css_class='form-group col-md-2'),
                Column('sluttvolum', css_class='form-group col-md-2'),
                Column('utbytte', css_class='form-group col-md-2'),
                css_class='form-row'
            ),
            Row(
                Column('mesketemperatur', css_class='form-group col-md-2'),
                Column('rating', css_class='form-group col-md-2'),
                Column('meskevann', css_class='form-group col-md-2'),
                Column('kokevolum', css_class='form-group col-md-2'),
                Column('etterfylling', css_class='form-group col-md-2'),
                Column('gjaer', css_class='form-group col-md-2'),
                css_class='form-row'
            ),
            Row(
                Column('malt_1', css_class='form-group col-md-3'),
                Column('m_mengde_1', css_class='form-group col-md-3'),
                Column('humle_1', css_class='form-group col-md-3'),
                Column('h_mengde_1', css_class='form-group col-md-3'),
                css_class='form-row'
            ),
            Row(
                Column('malt_2', css_class='form-group col-md-3'),
                Column('m_mengde_2', css_class='form-group col-md-3'),
                Column('humle_2', css_class='form-group col-md-3'),
                Column('h_mengde_2', css_class='form-group col-md-3'),
                css_class='form-row'
            ),
            Row(
                Column('malt_3', css_class='form-group col-md-3'),
                Column('m_mengde_3', css_class='form-group col-md-3'),
                Column('humle_3', css_class='form-group col-md-3'),
                Column('h_mengde_3', css_class='form-group col-md-3'),
                css_class='form-row'
            ),
            Row(
                Column('malt_4', css_class='form-group col-md-3'),
                Column('m_mengde_4', css_class='form-group col-md-3'),
                Column('humle_4', css_class='form-group col-md-3'),
                Column('h_mengde_4', css_class='form-group col-md-3'),
                css_class='form-row'
            ),
            Row(
                Column('malt_5', css_class='form-group col-md-3'),
                Column('m_mengde_5', css_class='form-group col-md-3'),
                Column('humle_5', css_class='form-group col-md-3'),
                Column('h_mengde_5', css_class='form-group col-md-3'),
                css_class='form-row'
            ),
            Row(
                Column('kommentar', css_class='form-group col-md-12'),
                css_class='form-row'
            ),
            Submit('submit', 'Submit', css_class = 'btn-primary')
        )

        def clean(self):
            all_clean_data = super().clean()
            a = all_clean_data['malt_1']
            b = all_clean_data['malt_2']
            c = all_clean_data['malt_3']
            d = all_clean_data['malt_4']
            e = all_clean_data['malt_5']
            self.meskevann = (a + b + c + d + e) * 3
            return self.meskevann

"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('bryggnr', 'dato', 'navn', css_class='form-group col-md-6'),
                Column('malt_1', 'malt_2', 'malt_3', 'malt_4', 'malt_5', 'malt_6', 'malt_7', 'malt_8', 'malt_9', 'malt_10', css_class='form-group col-md-3'),
                Column('mengde_1', 'mengde_2', 'mengde_3', 'mengde_4', 'mengde_5', 'mengde_6', 'mengde_7', 'mengde_8', 'mengde_9', 'mengde_10', css_class='form-group col-md-3'),
                css_class='form-row'
                ),
            Submit('submit', 'Submit', css_class = 'btn-primary')
        )
"""
