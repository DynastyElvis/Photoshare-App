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

# def gallery(request):#, category_id):
#     category = request.GET.get('category')
    
    
#     if category == 'None':
#         photos = Photo.objects.all()


#     else:
#         photos = Photo.objects.filter(category__name=category)

    
#     categories = Category.objects.all()
#     photos = Photo.objects.all()
    
#     context = {'categories': categories, 'photos': photos}
#     return render(request, 'photos/gallery.html', context)



def location(request):
    location = request.GET.get('location')
    if location == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(location__name = location)
        
    locations = Location.objects.all() 
    
    context = {'locations': locations, 'photos':photos}
    
    return render(request,'photos/location.html', context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request,'photos/photo.html',{'photo':photo})

def addPhoto(request):
    categories = Category.objects.all()
    
    
    
    # if request.method == 'POST':
    #     data = request.POST
    #     image = request.FILES.get('image')
        
    #     if data['category'] != 'none':
    #         category = Category.objects.get(id=data['category'])          
        
            
    #     elif data['category_new'] != '':
    #         category,created = Category.objects.get_or_create(name=data['category_new'])           
        
            
    #     else:
    #         category = None
            
    #     photo = Photo.objects.create(
    #         category=category,                      
    #         description=data['description'],            
    #         image=image,
    #     )
    #     return redirect ('gallery')
            
    context = {'categories': categories}    
    return render(request,'photos/add.html', context)
# def gallery(request):#, category_id):
#     category = request.GET.get('category')
    
    
#     if category == 'None':
#         photos = Photo.objects.all()


#     else:
#         photos = Photo.objects.filter(category__name=category)

    
#     categories = Category.objects.all()
#     photos = Photo.objects.all()
    
#     context = {'categories': categories, 'photos': photos}
#     return render(request, 'photos/gallery.html', context)

