from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
# import loader to load the template
from django.template import loader
# Create your views here.
# //function name becomes the name of view
# //takes the request and give response

# need to link this view with url
def index(request):
    item_list=Item.objects.all()
    # print("item_list - ",item_list)
    # template=loader.get_template('food/index.html')
    # //render a template
    context={
        'item_list':item_list,
    }
    # return HttpResponse(template.render(context,request))
    # no need of loader if use render
    return render(request,'food/index.html',context)

def item(request):
    return HttpResponse("<h1>Hello Items</h1>")

def detail(request,item_id):
    item=Item.objects.get(pk=item_id)
    context={
        'item':item,
    }
    return render(request,'food/detail.html',context)