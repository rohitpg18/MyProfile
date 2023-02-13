from django.shortcuts import render, redirect
from resume.models import Contact
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views import View

# def index(request):
    
#     if request.method == 'POST':
        
    
#         form = ContactForm(request.POST or None)

#         if form.is_valid():
#             form.save()
#             messages.success(request, "Submitted Successfully...!!!!")
#             # return HttpResponseRedirect('profile')

#         context = {
#             'form':form
#             }
        
#         return render(request, 'index.html', context)

class ProfileView(View):
    
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    
    def post(self, request, *args, **kwargs):
        
        Contact.objects.create(ur_name = request.POST['ur_name'], email_id = request.POST['email_id'], subject = request.POST['subject'], message = request.POST['message'])
        # return HttpResponseRedirect('profile')
        return redirect('profile')
        
        return render(request, 'index.html')