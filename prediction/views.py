from __future__ import unicode_literals
from django.shortcuts import render
from .forms import NameForm
from django.http import HttpResponseRedirect
from .prediction_code import plot1, plot2,plot3,plot4,plot5

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            graph1 = plot1(form.cleaned_data)
            graph2 = plot2(form.cleaned_data)
            graph3 = plot3(form.cleaned_data)
            graph4 = plot4(form.cleaned_data)
            graph5 = plot5(form.cleaned_data)

            return render(request, 'prediction/index.html', {'graph1': graph1, 'graph2': graph2, 'graph3': graph3, 'graph4': graph4, 'graph5': graph5})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'prediction/index.html', {'form': form})
