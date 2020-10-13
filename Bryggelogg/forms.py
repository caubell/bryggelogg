# General Django imports
from django import forms

# Model imports
from Bryggelogg.models import Bryggelogg, Recipes, Malt, Hop

# Crispy form specific imports
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit, Row, Column
import re


# Formset specific imports
from django.forms import ModelForm, inlineformset_factory
from .custom_layout_object import *

class RecipesForm(ModelForm):
    class Meta():
        model = Recipes
        exclude = ()
        labels = {'name': '', 'type': '', 'date': '', 'og': '', 'fg': '', 'abv': '', 'ibu': '', 'efficiency': '',
                  'batch_volume': '', 'mash_time': '', 'mash_temp': '', 'boil_time': '', 'boil_volume': '',
                  'fermenter_volume': '',  'yeast': '', 'link': '', 'malt': '', 'amount': ''}
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'type': forms.TextInput(attrs={'placeholder': 'Type'}),
            'date': forms.TextInput(attrs={'placeholder': 'Date'}),
            'og': forms.TextInput(attrs={'placeholder': 'OG'}),
            'fg': forms.TextInput(attrs={'placeholder': 'FG'}),
            'abv': forms.TextInput(attrs={'placeholder': 'ABV'}),
            'ibu': forms.TextInput(attrs={'placeholder': 'IBU'}),
            'efficiency': forms.TextInput(attrs={'placeholder': 'Efficiency'}),
            'batch_volume': forms.TextInput(attrs={'placeholder': 'Batch Size'}),
            'mash_time': forms.TextInput(attrs={'placeholder': 'Mashing Time (min)'}),
            'mash_temp': forms.TextInput(attrs={'placeholder': 'Mash Temperature'}),
            'boil_time': forms.TextInput(attrs={'placeholder': 'Boiling Time (min)'}),
            'boil_volume': forms.TextInput(attrs={'placeholder': 'Boil Volume'}),
            'fermenter_volume': forms.TextInput(attrs={'placeholder': 'Fermenter Volume'}),
            'yeast': forms.TextInput(attrs={'placeholder': 'Yeast'}),
            'link': forms.TextInput(attrs={'placeholder': 'URL'}),
            'malt': forms.TextInput(attrs={'placeholder': 'Malt'}),
            'amount': forms.TextInput(attrs={'placeholder': 'Amount'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6'),
                Column('type', css_class='form-group col-md-3'),
                Column('link', css_class='form-group col-md-3'),
                css_class='form-row'
                ),
            Row(
                Column('batch_volume', css_class='form-group col-md-2'),
                Column('mash_time', css_class='form-group col-md-2'),
                Column('mash_temp', css_class='form-group col-md-2'),
                Column('boil_time', css_class='form-group col-md-2'),
                Column('boil_volume', css_class='form-group col-md-2'),
                Column('fermenter_volume', css_class='form-group col-md-2'),
                css_class='form-row'
            ),
            Row(
                Column('og', css_class='form-group col-md-2'),
                Column('fg', css_class='form-group col-md-2'),
                Column('abv', css_class='form-group col-md-2'),
                Column('ibu', css_class='form-group col-md-2'),
                Column('efficiency', css_class='form-group col-md-2'),
                Column('yeast', css_class='form-group col-md-2'),
                css_class='form-row'
                ),
            Row(
                Column(Formset_malt('malt'), css_class='form-group col-md-6'),
                Column(Formset_hop('hop'), css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            Row(
                Column('note', css_class='form-group col-md-12'),
                css_class='form-row'
                ),

            Submit('submit', 'Submit', css_class = 'btn-primary')
        )

class MaltForm(ModelForm):
    class Meta():
        model = Malt
        exclude = ()
        labels = {'malt': '', 'amount': ''}
        widgets = {
            'malt': forms.TextInput(attrs={'placeholder': 'Malt'}),
            'amount': forms.TextInput(attrs={'placeholder': 'Amount'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        formtag_prefix = re.sub('-[0-9]+$', '', kwargs.get('prefix', ''))

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
                Row(
                    Column('malt', css_class='col-md-5'),
                    Column('amount', css_class='col-md-5'),
                    Div('DELETE'),
                    css_class='formset_row-{}'.format(formtag_prefix)
                )
            )

MaltFormSet = inlineformset_factory(Recipes, Malt, form = MaltForm, extra = 1)

class HopForm(ModelForm):
    class Meta():
        model = Hop
        exclude = ()
        labels = {'hop': '', 'amount': ''}
        widgets = {
            'hop': forms.TextInput(attrs={'placeholder': 'Hop'}),
            'amount': forms.TextInput(attrs={'placeholder': 'Amount'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        formtag_prefix = re.sub('-[0-9]+$', '', kwargs.get('prefix', ''))

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
                Row(
                    Column('hop', css_class='col-md-5'),
                    Column('amount', css_class='col-md-5'),
                    Field('DELETE'),
                    css_class='formset_row-{}'.format(formtag_prefix)
                )
            )

HopFormSet = inlineformset_factory(Recipes, Hop, form = HopForm, extra = 1)

class BryggeloggForm(forms.ModelForm):

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

        self.helper = FormHelper()
        self.helper.form_tag = True
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
