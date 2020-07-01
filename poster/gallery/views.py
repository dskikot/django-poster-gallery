from django.views.generic import ListView, DetailView
from .models import Category, Tag, Image


class IndexList(ListView):
    model = Image
    template_name = 'gallery/index.html'
    context_object_name = 'images'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все работы'
        context['categories'] = Category.objects.all()
        return context


class ImagesByCategory(ListView):
    template_name = 'gallery/index.html'
    context_object_name = 'images'
    paginate_by = 6
    allow_empty = False

    def get_queryset(self):
        return Image.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Работы по категории: ' + str(Category.objects.get(slug=self.kwargs['slug']))
        context['categories'] = Category.objects.all()
        return context


class ImagesByTag(ListView):
    template_name = 'gallery/index.html'
    context_object_name = 'images'
    paginate_by = 6
    allow_empty = False

    def get_queryset(self):
        return Image.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Работы по тегу: ' + str(Tag.objects.get(slug=self.kwargs['slug']))
        context['categories'] = Category.objects.all()
        return context


class ImageDetail(DetailView):
    model = Image
    template_name = 'gallery/image_detail.html'
    context_object_name = 'image'