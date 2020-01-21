from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import article
from django.db import connection

cursor = connection.cursor()


def article_main(request):
    if request.method == 'GET' :
    
        page = int(request.GET.get("page",1))    
        list1 = article.objects.all()[page*6-6:page*6]
        cnt = article.objects.all().count()
        total = (cnt-1)//6+1    

        
        imgs = ["/static/image/art_thumbnail/['newsis' + str(i) + '.png']"]
        for i in imgs :
            

            
        



        return render(request,'article_main2.html',{"list":list1, "pages":range(1,total+1,1)}, "img":img)
        # return render(request,'article_main.html',{"list":rows, 'img': "/static/image/art_thumbnail/['newsis' + str(i) + '.png']", "cnt":range(60)})
     

