from django.shortcuts import render

from . models import Photo_Album

# Create your views here.
def index(request):

    # query objects/items from the DB
    photo = Photo_Album.objects.all()

    cloudinary_img = {'photos': photo}

    return render(request,'photo/index.html', cloudinary_img)

