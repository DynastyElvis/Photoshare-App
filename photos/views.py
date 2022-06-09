from django.shortcuts import render, redirect
from .models import Category, Photo, Location


# def gallery(request):#, category_id):
#     category = request.GET.get('category')
    

def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name = category)
        
    categories = Category.objects.all()   
    locations = Location.objects.all()  
    
    
    context = {'categories': categories, 'photos':photos, 'locations': locations}
    
    return render(request,'photos/gallery.html', context)

def gallery(request):#, category_id):
    category = request.GET.get('category')
    
    
    if category == 'None':
        photos = Photo.objects.all()


    else:
        photos = Photo.objects.filter(category__name=category)

    
    categories = Category.objects.all()
    photos = Photo.objects.all()
    
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html', context)


