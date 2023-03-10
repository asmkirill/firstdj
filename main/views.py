from django.shortcuts import render

def index(request):
    data = {
        'title': 'Main page',
        'obj': {
            'car': "BMW",
            'pet': 'cat',
            'age': 18
        },
        'device': 'hummer'
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')