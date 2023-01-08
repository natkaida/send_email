from django.views.generic import FormView, TemplateView
from .forms import ContactForm
from django.urls import reverse_lazy

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('yandex:success')

    def form_valid(self, form):
        form.send()
        return super().form_valid(form)

class ContactSuccessView(TemplateView):
    template_name = 'success.html'        