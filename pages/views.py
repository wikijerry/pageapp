from django.shortcuts import render
from django.views.generic import TemplateView

class HomepageView(TemplateView):
    template_name = "home.html"

class AboutpageView(TemplateView):
    template_name = "about.html"


'''npm uninstall -g heroku-cli
npm i -g heroku 
pip install node'''