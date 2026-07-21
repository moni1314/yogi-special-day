from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def letter(request):
    return render(request, 'letter.html')

def gallery(request):
    return render(request, 'gallery.html')
def video(request):
    return render(request, 'video.html')
def cake(request):
    return render(request, 'cake.html')
def final(request):
    return render(request, 'final.html')
def video(request):
    return render(request, "video.html")
def gift(request):
    return render(request, "gift.html")
def family(request):
    return render(request, "family.html")
def certificate(request):
    return render(request, "certificate.html")