from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={"slug": self.slug})


class Image(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    filename = models.ImageField(upload_to='img/', blank=True, verbose_name='Имя файла')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='images', verbose_name='Категория')
    tags = models.ManyToManyField(Tag, blank=True, related_name='images', verbose_name='Теги')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('image', kwargs={'pk': self.pk})

    def get_tags(self):
        tags = self.tags.all()
        result = ''
        for tag in tags:
            result += ', ' + tag.title
        return result  # ', '.join(tags.title)
