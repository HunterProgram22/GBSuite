from django.shortcuts import render, HttpResponse

def main(request):
    return render(request, 'GBFinance/mainhome.html', {})
    #return HttpResponse('Main project page')