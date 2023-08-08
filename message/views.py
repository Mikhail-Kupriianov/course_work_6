from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from message.forms import MessageForm
from message.models import Message
from users.models import User


class MessageListView(LoginRequiredMixin, ListView):
    paginate_by = 4
    model = Message
    extra_context = {
        'title': 'Сообщения'
    }


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        context_data['title'] = context_data['object']
        return context_data


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    # fields = ('message_title', 'message_content',)
    success_url = reverse_lazy('message:messages')

    def get_initial(self):
        initials = super().get_initial()
        initials['message_owner'] = User.objects.get(email=self.request.user)
        return initials


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    fields = ('message_title', 'message_content',)

    def get_success_url(self):
        return reverse('message:message_item', kwargs={'pk': self.object.pk})


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('message:messages')
