from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home/home.html'

class AboutPageView(TemplateView):
    template_name = 'home/about.html'




