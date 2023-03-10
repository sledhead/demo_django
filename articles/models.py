from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField( blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)


    def save(self, *args, **kwargs):

        #if self.slug is None:
            #self.slug = slugify(self.title)

        super().save(*args, **kwargs)


def slugify_instance_title(instance, save=False):
    
    slug = slugify(instance.title)
    qs = Article.objects.filter(slug=slug).exclude(id=instance.id)
    if(qs.exists()):
        #make new slug
        slug = f"{slug}-{qs.count() + 1}"
        
    instance.slug = slug

    if(save == True):
        instance.save()

def article_pre_save(sender, instance, *args, **kwargs):
    print('pre_save')
    

    if instance.slug is None:
        slugify_instance_title(instance)

pre_save.connect(article_pre_save, sender=Article)


def article_post_save(sender, instance, created, *args, **kwargs):
    print('post_save')
    
    if( created == True):
        slugify_instance_title(instance,save=True)

post_save.connect(article_post_save, sender=Article)