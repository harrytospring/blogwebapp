from django.shortcuts import render
from django.http import HttpResponse
from .models import blog_content
from django.template import RequestContext,loader

def index(request):
	return HttpResponse("hello,this is the first site")
def blog(request,head):
	blogheadlist = blog_content.objects.values("blog_head","blog_text")
	template = loader.get_template('blogcontent/blogcontent.html')
	b=[]
	for i in blogheadlist:
		b.append(i)
	context=RequestContext(request,{
		'i':b[int(head)],
		'head':int(head),
		})
	return HttpResponse(template.render(context))
def bloglist(request):
	bloglist = blog_content.objects.values("blog_head")
	blog_num = blog_content.objects.count()
	b=[]
	for a in bloglist:
		b.append(a['blog_head'])
	template = loader.get_template('blogcontent/index.html')
	context = RequestContext(request,{
		'b':b,
		'blog_num': blog_num,
		})
	return HttpResponse(template.render(context))



# Create your views here.
