from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Patent
from .forms import PatentCreateForm, PatentUpdateForm


class PatentListView(ListView):
    model = Patent
    template_name = 'patents/patent_list.html'
    context_object_name = 'patents'
    paginate_by = 10


class PatentDetailView(DetailView):
    model = Patent
    template_name = 'patents/patent_detail.html'
    context_object_name = 'patent'


class PatentCreateView(CreateView):
    model = Patent
    template_name = 'patents/patent_edit.html'
    context_object_name = 'patent'
    form_class = PatentCreateForm
    success_url = reverse_lazy('patent_list')


class PatentUpdateView(UpdateView):
    model = Patent
    template_name = 'patents/patent_edit.html'
    context_object_name = 'patent'
    form_class = PatentUpdateForm
    success_url = reverse_lazy('patent_list')


class PatentDeleteView(DeleteView):
    model = Patent
    template_name = 'patents/patent_delete.html'
    success_url = reverse_lazy('patent_list')