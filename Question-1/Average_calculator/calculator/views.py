from django.shortcuts import render
from django.http import JsonResponse

def calculator(request):
    access_token = request.GET.get('settings.ACCESS_TOKEN')
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')

    if num1 is not None and num2 is not None:
        try:
            average = (float(num1) + float(num2)) / 2 
            return JsonResponse({'average': average})
        except ValueError:
            return JsonResponse({'error': 'Invalid input. Please provide valid numbers.'}, status=400)

    return render(request, 'index.html')