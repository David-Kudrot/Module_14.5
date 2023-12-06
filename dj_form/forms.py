from django import forms

import datetime


class FormAPI(forms.Form):
    name = forms.CharField(max_length=20)
    
    #initial_values
    first_name_with_initial_value = forms.CharField(
        initial='Enter your first name'
    )
    all_okay = forms.BooleanField(initial=True)
    #date as initial value
    day = forms.DateField(initial=datetime.date.today)
    
    name_with_max_length_50 = forms.CharField(
        max_length=50
    )
    
    email = forms.EmailField()
    #email with label
    email_with_label = forms.EmailField(
        label="Label : Please enter your email address"
    )
    email_address_not_required_or_optional = forms.EmailField(
        required=False
    )
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    verify = forms.BooleanField()
    date = forms.DateField()
    date_with_Number_or_birthday = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))# we can also import "from django.forms.widgets import NumberInput"
    
    # eta theke years select kora jabe[Good I like it]
    CHOICE_YEARS = ['1995', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026']
    wow_date_with_select_field_widgets = forms.DateField(widget=forms.SelectDateWidget(years=CHOICE_YEARS))
    
    value_or_number = forms.DecimalField()
    
    
    #choise field
    CHOOSE_COLOR = [
        ('red', 'Red'),
        ('green', 'Green'),
        ('blue', 'Blue'),
        ('purple', 'Purple'),
        ('yellow', 'Yellow'),
        ('white', 'White'),
        ('black', 'Black'),
    ]
    
    choose_color = forms.ChoiceField(choices=CHOOSE_COLOR)
    #choise field with radio 
    choose_Your_color = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOOSE_COLOR)
    
    #multiple chosie field
    FRUIT_NAMES = [
        ('apple', 'Apple'),
        ('orange', 'Orange'),
        ('banana', 'Banana'),
        ('blackberry', 'Blackberry'),
        ('papaya', 'Papaya'),
        ('date', 'Date'),
        ('lemon', 'Lemon'),
    ]
    choose_multiple_fruit = forms.MultipleChoiceField(choices=FRUIT_NAMES)
    choose_fruit_multiple_by_radio = forms.ChoiceField(widget=forms.RadioSelect, choices=FRUIT_NAMES)
    choose_fruit_multiple_by_checkbox = forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices=FRUIT_NAMES)