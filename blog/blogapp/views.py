from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import ContextMixin

from .models import Post, Tag
from .forms import ContactForm, PostForm


# Create your views here.
def main_view(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/index.html', context={'posts': posts})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Получить данные из формы
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            
            send_mail(
                'Contact message',
                f' Ваше сообщение {message} принято',
                'from@example.com',
                [email],
                fail_silently=True,
            )

            return HttpResponseRedirect(reverse('blogapp:index'))
        else:
            return render(request, 'blogapp/contact.html', context={'form': form})
    else:
        form = ContactForm()
        return render(request, 'blogapp/contact.html', context={'form': form})

def  post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blogapp/post.html', context={'post': post})

def create_post(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'blogapp/create.html', context={'form': form})
    else:
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid():            
            form.save()
            return HttpResponseRedirect(reverse('blogapp:index'))
        else:
            return render(request, 'blogapp/create.html', context={'form': form})
        
class NameContextMixin(ContextMixin):
        # Отвечает за передачу параметров
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Теги'
        return context
        
# CRUD - CREATE, READ (LIST, DEATAIL), UPDATE, DELETE
# Список тегов
class TagListView(ListView, NameContextMixin):
    model = Tag
    template_name = 'blogapp/tag_list.html'
    context_object_name ='tags'

   
    # Получение данных
    def get_queryset(self):
        return Tag.objects.all()

# Детальная информация
class TagDetailView(DetailView, NameContextMixin):
    model = Tag
    template_name = 'blogapp/tag_detail.html'

    # Метод обработки get запроса
    def get(self, request, *args, **kwargs):
        self.tag_id = kwargs['pk']
        return super().get(request, *args, **kwargs)

    # Отвечает за передачу параметров
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Теги'
        return context
    
    # Получение этого объекта
    def get_object(self, queryset = None):
        return get_object_or_404(Tag, pk=self.tag_id)

# Создание тега
class TagCreateView(CreateView, NameContextMixin):
    # from_class
    fields = '__all__'
    model = Tag
    success_url = reverse_lazy('blog:tag_list')
    template_name = 'blogapp/tag_create.html'

    # Пришел post запрос
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    # Метод срабатывает после того как форма валидна
    def form_valid(self, form):
        return super().form_valid(form)

class TagUpdateView(UpdateView):
    # from_class
    fields = '__all__'
    model = Tag
    success_url = reverse_lazy('blog:tag_list')
    template_name = 'blogapp/tag_create.html'

class TagDeleteView(DeleteView):
    template_name = 'blogapp/tag_delete_confirm.html'
    model = Tag
    success_url = reverse_lazy('blog:tag_list')