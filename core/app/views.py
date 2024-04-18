from django.shortcuts import render, redirect, get_object_or_404
from app.forms import MediaForm
from app.models import Media
from django.views.generic import TemplateView,ListView,DetailView,DeleteView,UpdateView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from app.forms import MediaForm




def main_page(request):
    return render(request,'app/main_page.html')






class UploadMediaView(CreateView):
    template_name = 'app/upload_media.html'
    form_class = MediaForm
    success_url = reverse_lazy('movies')
    
    
    


class SignUpView(CreateView):
    template_name = 'app/sign_up.html'
    
    form_class = UserCreationForm
    success_url = reverse_lazy('main_page')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main_page')
        return super().get(request, *args, **kwargs)

class UserLoginView(LoginView):
    template_name = 'app/login.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('main_page')

def user_logout(request):
    logout(request)
    return redirect('main_page')


@login_required
def list_view(request):
    media_list = Media.objects.all()
    context = {'media_list': media_list}
    return render(request, 'app/list_page.html',
                  context=context)

@login_required
def detail_view(request, pk):
    media = get_object_or_404(Media, pk=pk)
    context = {'media_detail': media}
    return render(request, 'app/detail_page.html', context)


