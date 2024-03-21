from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

def mainpage(request):
   return render(request, "main.html")

# class Profil(View):
#     context = {}
#     template_name = "profil.html"
    
#     def get(self, request):
#         return render(request, self.template_name, self.context)
    
#     def post(self, request):
#         return render(request, self.template_name, self.context)