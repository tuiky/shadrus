from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from article.models import Article, Comments

# Create your views here.

def basic_one(request):
	view = 'basic_one'
	html = '<html><body><h1>this is %s view </h1></html></body>' % view
	return HttpResponse(html)

def template_two(request):
	view ="template_two_super-puper_name"
	t = get_template('myview.html')
	html = t.render(
					Context(
							{'name':view}
							)
					)
	return HttpResponse(html)

def template_three_simple(request):
	view = 'actual type of return template'
	return render_to_response('myview.html',{'name':view})

def articles(request):
	return render_to_response('articles.html',{'articles': Article.objects.all()})

def article(request, article_id=1):
	return render_to_response('article.html', {'article': Article.objects.get(id=article_id), 'comments': Comments.objects.filter(comments_article_id=article_id)})