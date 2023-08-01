from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name = category)

    categories = Category.objects.all()
    context = {
        'categories': categories,
        'photos': photos,
    }
    return render(request, 'snaps/gallery.html', context)

def addPhoto(request):
    categories = Category.objects.all()

    if(request.method == 'POST'):
        data = request.POST
        image = request.FILES.get('image')

        if(data['category'] != 'none'):
            category = Category.objects.get(id = data['category'])
        elif(data['category_new'] != ''):
            category, created = Category.objects.get_or_create(name = data['category_new'])
        else:
            category = None

        photo = Photo.objects.create(category=category, description=data['description'], image=image)

        return redirect('gallery')

    return render(request, 'snaps/add.html', {'categories': categories})

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'snaps/photo.html', {'photo': photo})