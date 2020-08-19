from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.urls import reverse
from PIL import Image
# Create your models here.


class BookManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = Q(title__icontains=query)
            qs = qs.filter(or_lookup).distinct()  # distinct() is often necessary with Q lookups
        return qs


class Genre(models.Model):
    name = models.CharField(max_length=50, verbose_name='Genre Name')

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=20, verbose_name='Language Name')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50, verbose_name='书名')
    author = models.CharField(max_length=50, verbose_name='作者')
    publication = models.CharField(max_length=100, verbose_name='出版商')
    image = models.ImageField(verbose_name='封面', null=True, blank=True)
    description = models.TextField(max_length=1000, verbose_name='描述', null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='价格')
    contact_number = models.CharField(max_length=40, verbose_name='联系方式')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='更新时间')
    genre = models.ForeignKey(Genre, related_name='books', related_query_name='book', on_delete=models.CASCADE, verbose_name='分类')
    language = models.ForeignKey(Language, related_name='books', related_query_name='book', on_delete=models.CASCADE, verbose_name='语言')
    created_by = models.ForeignKey(User, related_name='book', related_query_name='book', on_delete=models.CASCADE)

    objects = BookManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})
        # return reverse('book_edit', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:
        ordering = ['-created_at']
