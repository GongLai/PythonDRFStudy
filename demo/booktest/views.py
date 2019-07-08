from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json

from .models import BookInfo


class BookView(View):
    """获得一本书的书本对象"""

    def get(self, request):
        # 1.数据处理
        # 1.1 获得单一的书本对象
        book = BookInfo.objects.all()[0]
        # 1.2将该对象组织成字典
        book_dict = ({
            "id": book.id,
            "btitle": book.btitle,
            "bpub_date": book.bpub_date,
            "bread": book.bread,
            "bcomment": book.bcomment,
            "image": book.image.url if book.image else ''
        })
        # 2.页面渲染--将该字典传入到模板中[前后端不分离]
        # return render(request, 'index.html', context=book_dict)

        # 2.返回json格式的数据[前后端分离]
        return JsonResponse(book_dict)


"""
总结: 
前后端不分离 >> 数据处理与页面渲染全部由后端完成,再返回给前端
前后端分离 >> 后端只负责数据处理,返回JSON格式数据给前端,由前端自行负责渲染页面
"""

