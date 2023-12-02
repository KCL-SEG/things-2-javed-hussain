from django.test import TestCase
from .forms import ThingsForm
from django import forms

class ThingsFormTest(TestCase):
    def setUp(self):
        self.form_input = {
            'name': 'javed',
            'description' : 'i am a human',
            'quantity' : '10',
        }
    def test_valid_sign_up_form(self):
        form = ThingsForm(data = self.form_input)

        self.assertTrue(form.is_valid())

    def test_form_has_neccesary_feilds(self):
        form = ThingsForm()
        self.assertIn("name", form.fields)
        self.assertIn("description", form.fields)
        description_widget = form.fields['description'].widget
        self.assertTrue(isinstance(description_widget, forms.Textarea))
        self.assertIn("quantity", form.fields)
        quantity_widget = form.fields['quantity'].widget
        self.assertTrue(isinstance(quantity_widget, forms.NumberInput))
    
    
