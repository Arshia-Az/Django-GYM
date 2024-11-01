from django.shortcuts import render
from .forms import ContactForm
from django.views.generic import View
# Create your views here.


class ContactUsView(View):

    # TODO """
    #  this we have huge problem because its not have login and register page and any one can send the information
    #  we can create login or regester page or we can check the email from google
    #  """

    def get(self, request):
        form = ContactForm()

        context = {
            'form': form,
        }
        return render(request, 'contact_us/contact.html', context)

    def post(self, request):
        form = ContactForm(request.POST or None)
        if form.is_valid():

            form.save()
        context = {
            'form': form,
        }
        return render(request, 'contact_us/contact.html', context)