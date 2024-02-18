from django.shortcuts import render
from django.utils import timezone
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
import markdown
from mainapp.settings import BASE_DIR
from .forms import PartialContactusForm
from .models import Contactus
from . import menu

home_template              = 'index.html'
aboutus_template           = 'common/aboutus.html'
disclaimar_template        = 'common/disclaimer.html'
contactus_template         = 'contactus.html'
contactus_thanks_template  = 'contactus_thanks.html'
profile_template           = 'profile.html'

def homepage(request):
    return render(request, home_template, menu.get_navbar('Home'))

def aboutus(request):
    return render(request, aboutus_template, menu.get_navbar('About Us'))

def disclaimar(request):
    return render(request, disclaimar_template, menu.get_navbar('Disclaimer'))

# Display profile feature

@login_required
def profile(request):
    items = menu.get_navbar('Profile')
    social_info = SocialAccount.objects.filter(user=request.user)
    if social_info and (len(social_info) > 0):
        items['profile'] = social_info[0]       
    return render(request, profile_template, items)

# Feedback feature - a.k.a CONTACT US

@login_required
def contactus(request):
    items = menu.get_navbar('Contact Us')
    items['form'] = PartialContactusForm()
    return render(request, contactus_template, items)

def contactus_post(request):
    items = menu.get_navbar('Contact Us')
    contactus = Contactus(user=request.user.username, tm=timezone.now())
    form = PartialContactusForm(request.POST, instance=contactus)
    if form.is_valid():
        try:
            form = form.save()
            items['form'] = form
            return render(request, contactus_thanks_template, items)
        except Exception as e:
            print('%s' % type(e))
            pass
    items['form'] = form
    return render(request, contactus_template, items)

# Display markdown documentation 

default_md = "step1.md"
menu_key = "Get Started"
query_param = "doc_name"
makdown_template = "markdown.html"
template_context = "markdown"


def get_default(request):
    return get_doc(request, default_md)

def get_doc(request, doc_name):
    if not doc_name:
        doc_name = default_md
    context = menu.get_navbar(menu_key)
    context[query_param] = doc_name
    download_doc = f"{BASE_DIR}/home/templates/docs/{doc_name}"
    md = markdown.Markdown(extensions=["fenced_code"])
    with open(download_doc, 'r') as file:
        text = file.read()
        html = md.convert(text)
        context[template_context] = html
    file.closed
    return render(request, makdown_template, context)


theme_key = "Theme"
default_template = "nest-theme"
folder = "theme-doc"

def get_theme_default(request):
    return get_theme(request, default_template)

def get_theme(request, theme_name):
    if not theme_name:
        theme_name = default_template
    return render(request, f'{folder}/{theme_name}.html', menu.get_navbar(theme_key))
