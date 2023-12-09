from django.shortcuts import render
from dj_form.forms import FormAPI
from dj_form.forms2 import Form2
# from . forms import FormAPI

# Create your views here.



def home(request):
    return render(request, 'home.html')

def form_api(request):
    form = FormAPI(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'formApi.html', {'form': form})

def model_forms(request):
    model_forms = Form2()
    return render(request, 'modelForm.html', {'form': model_forms})