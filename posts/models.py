from django.contrib import admin
from django.db import models

# Model for the posts app

class Post(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    pageName = models.CharField(max_length=256, blank=True)

    def __unicode__(self):
        return self.title

class PostImage(models.Model):
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to='static/uploads', height_field='height', width_field='width')
    width = models.IntegerField(editable=False)
    height = models.IntegerField(editable=False)
    post = models.ForeignKey(Post)

### Admin

#class PostImageAdmin(admin.ModelAdmin):
#    search_fields = ["title"]

class PostImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'width', 'height')

admin.site.register(Post)
admin.site.register(PostImage, PostImageAdmin)
