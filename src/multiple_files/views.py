# views.py
# -*- coding: utf-8 -*-
from django.shortcuts import redirect, render
from django.shortcuts import render_to_response

from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import View

from .models import Attachment, Object

class ObjectView(View):
    
    def post(self, request):
        name = request.POST.get('name', '')
        desc = request.POST.get('description', '')
        
        obj = Object.objects.create(name=name, description=desc)
        if obj is not None:
            return JsonResponse({'id':obj.id})
        else:
            return JsonResponse({'status':'error', 'message':'cant create object'}, status=400)
        
class AttachmentView(View):

    def get(self, request):
        return render(request, "multiple_files/add_attachment.html")
    
    def post(self, request):
        obj_id = int(request.POST.get('id', ''))
        print request.FILES
        for a_file in request.FILES.itervalues():
            instance = Attachment(
                attachment=a_file
            )
            instance.object_id = obj_id
            instance.save()
            
        # TODO: check on errors
        return JsonResponse({'status':'ok'})