from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from client.forms import ClientForm
from client.models import Client
from users.models import User


class ClientListView(LoginRequiredMixin, ListView):
    paginate_by = 4
    model = Client
    extra_context = {
        'title': 'Клиенты'
    }


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        context_data['title'] = context_data['object']
        return context_data


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:client')

    def get_initial(self):
        initials = super().get_initial()
        initials['client_owner'] = User.objects.get(email=self.request.user)
        return initials


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ('client_second_name', 'client_first_name', 'client_surname', 'client_email', 'client_comments')

    def get_success_url(self):
        return reverse('client:client_item', kwargs={'pk': self.object.pk})


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('client:client')

