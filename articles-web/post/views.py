from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from .models import Post, Category
from .forms import ContactForm


def index(request):
    articles = Post.objects.filter(status='published').order_by('-publication_data')
    categories = Category.objects.all()

    template = loader.get_template('index.html')
    context = {
        'articles': articles,
        'categories': categories
    }
    return HttpResponse(template.render(context, request))


def category(request, category_slug):
    articles = Post.objects.filter(status='published').order_by('-publication_data')
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        articles = articles.filter(category=category)

    template = loader.get_template('category.html')
    context = {
        'articles': articles,
        'categories': categories
    }

    return HttpResponse(template.render(context, request))


def tags(request, tag_slug):
    tags = Tag.objects.all()
    articles = Post.objects.filter(status='published').order_by('-publication_data')

    if tag_slug:
        tag = get_object_or_404(Tag, tag=tag_slug)
        articles = articles.filter(tags=tag)

    template = loader.get_template('tags.html')
    context = {
        'articles': articles,
    }

    return HttpResponse(template.render(context, request))


def post_details(request, post_slug):
    article = get_object_or_404(Post, slug=post_slug)

    template = loader.get_template('post_detail.html')

    context = {
        'article': article
    }

    return HttpResponse(template.render(context, request))


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.message_date = timezone.now()
            form.save()
            return redirect('contact-success')
    else:
        form = ContactForm()

    context = {
        'form': form
    }

    return render(request, 'contact.html', context)


def contact_success(request):
    return render(request, 'contactsuccess.html')
