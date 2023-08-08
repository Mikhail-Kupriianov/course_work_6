from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.forms import DistributionForm, CDCrossForm
from main.models import Distribution, CDCross
from main.utils.autosend_mail import DistributionMessages
from users.models import User


def index(request):
    mes_1 = DistributionMessages('Тестовое письмо', 'Это предложение исключительно для Вас!', 'Олег', 'dviod@yandex.ru')
    mes_1.send_email_message()
    return render(request, 'main/index.html')


class DistributionListView(LoginRequiredMixin, ListView):
    paginate_by = 4
    model = Distribution
    extra_context = {
        'title': 'Рассылки'
    }


class DistributionDetailView(LoginRequiredMixin, DetailView):
    model = Distribution

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        context_data['title'] = context_data['object']
        client_formset = inlineformset_factory(Distribution, CDCross, form=CDCrossForm, fields='__all__', extra=0)
        context_data['formset'] = client_formset(instance=self.object)
        return context_data


class DistributionCreateView(LoginRequiredMixin, CreateView):
    model = Distribution
    form_class = DistributionForm
    # fields = ('message_title', 'message_content',)
    success_url = reverse_lazy('main:distributions')

    def get_initial(self):
        initials = super().get_initial()
        initials['distribution_owner'] = User.objects.get(email=self.request.user)
        return initials


class DistributionUpdateView(LoginRequiredMixin, UpdateView):
    model = Distribution
    form_class = DistributionForm

    # fields = ('distribution_start', 'distribution_end', 'distribution_is_active', 'periodicity', 'status',
    #           'distribution_owner', 'distribution_message')

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        client_formset = inlineformset_factory(Distribution, CDCross, form=CDCrossForm, fields='__all__', extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = client_formset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = client_formset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('main:distribution_item', kwargs={'pk': self.object.pk})


class DistributionDeleteView(LoginRequiredMixin, DeleteView):
    model = Distribution
    success_url = reverse_lazy('main:distributions')
