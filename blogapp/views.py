from django.shortcuts import render

from django.shortcuts import render, redirect

SECRET_PASSWORD = "soniya"   # change this

def lock_page(request):
    if request.method == "POST":
        password = request.POST.get("password")

        if password == SECRET_PASSWORD:
            return redirect('secret')
        else:
            return render(request, 'lock.html', {'error': 'Wrong password 😢'})

    return render(request, 'lock.html')


def secret_page(request):
    return render(request, 'love_secret.html')
