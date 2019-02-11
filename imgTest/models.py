from django.db import models
class IMG(models.Model):
    # upload_to為圖片上傳的路徑，不存在就創建一個新的。
    img_url = models.ImageField(upload_to='img')
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

@receiver(pre_delete, sender=IMG)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.file.delete(False)
    
from django.db import models

class Image(models.Model):

    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.photo.name    