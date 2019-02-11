from django.shortcuts import render
from .models import IMG
from .models import Image

import random
from .form import UploadImageForm
from django.http import HttpResponse
# from PIL import Image
# Create your views here.
def uploadImg(request):
    if request.method == 'POST':
        img = IMG(img_url=request.FILES.get('img'))
        img.save()
    return render(request, 'imgupload.html')

# 顯示圖片
def showImg(request):
    imgs = IMG.objects.all()
    context = {
        'imgs' : imgs
    }
    return render(request, 'showImg.html', context)


def index(request):
    """图片的上传"""
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            picture = Image(photo=request.FILES['image'])
            picture.save()

            #lab = imageclassify(picture)
            return render(request, 'show.html', {'picture': picture})

    else:
        form = UploadImageForm()

        return render(request, 'index.html', {'form': form})

