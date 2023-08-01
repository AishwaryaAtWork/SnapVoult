from django.shortcuts import render

# Create your views here.
def gallery(request):
    return render(request, 'snaps/gallery.html')

def addPhoto(request):
    return render(request, 'snaps/add.html')

def viewPhoto(request, pk):
    return render(request, 'snaps/photo.html')