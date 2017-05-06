from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters

from django.views.generic.edit import FormView

from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from jobs.models import Job, About

class IndexView(generic.ListView):
    template_name = 'jobs/index.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        """ Return the last five published questions."""
        return Job.objects.order_by('-pub_date')

class DetailView(generic.DetailView):
    model = Job
    template_name = 'jobs/details.html'

    def get_queryset(self):
        """
        Excludes any jobs that aren't published yet.
        """
        return Job.objects.filter(pub_date__lte=timezone.now())

class AboutView(generic.DetailView):
    model = About
    template_name = 'jobs/about.html'

    def get_object(self):
        """
        Gets latest about entry
        """
        return About.objects.latest('pub_date') 

# TODO: Finish 404 and login views

# class FileNotFound():
#     def raise404():
#         raise Http404
 
class Login(FormView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'

    def form_valid(self, form):
        redirect_to = settings.LOGIN_REDIRECT_URL
        auth_login(self.request, form.get_user())
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
        return HttpResponseRedirect(redirect_to)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    @method_decorator(sensitive_post_parameters('password'))
    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()
        return super(Login, self).dispatch(request, *args, **kwargs)

class Logout(generic.DetailView):
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)