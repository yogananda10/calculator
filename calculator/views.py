from django.shortcuts import render
from django.http import HttpResponse
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error! Division by zero"
    return a / b


def home(request):
    result = None
    error = None

    if request.method == 'POST':
        try:
            a = int(request.POST.get("Num1"))
            b = int(request.POST.get("Num2"))
            choice = int(request.POST.get("choice"))

            if choice == 1:
                result = add(a, b)
            elif choice == 2:
                result = subtract(a, b)
            elif choice == 3:
                result = multiply(a, b)
            elif choice == 4:
                result = division(a, b)
            else:
                error = "Invalid choice"

        except ValueError:
            error = "Please enter valid numbers"

    return render(request, "index.html", {"result": result, "error": error})