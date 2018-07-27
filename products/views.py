from django.shortcuts import render
from .form import ContactForm




def home(request):
    return render(request, 'home.html')


def contact_page(request):
    form = ContactForm(request.POST or None)
    context = {
        "tittle" :"contact",
        "content":"welcome to contact page",
        "form": form
    }
    if form.is_valid():
        print (form.cleaned_data)
    if request.method =='POST':
        print(request.POST.get('fullname'))
        print (request.POST.get('email'))
        print (request.POST.get('contain'))

    return render(request, 'contact_page.html',context)


def login_page(request):
    return render(request,'login.html')
