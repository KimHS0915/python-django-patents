from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from .models import Patent
from .forms import PatentForm


def patent_list(request):
    patents = Patent.objects.all().order_by('publication_number')

    paginator = Paginator(patents, 10)
    page_number = request.GET.get('page')
    page_objects = paginator.get_page(page_number)

    return render(request, 'patents/patent_list.html', {'patents': page_objects})


def patent_detail(request, pk):
    patent = get_object_or_404(Patent, pk=pk)
    return render(request, 'patents/patent_detail.html', {'patent': patent})

def patent_new(request):
    if request.method == 'POST':
        form = PatentForm(request.POST)
        if form.is_valid():
            patent = form.save()
            return redirect('patent_detail', pk=patent.pk)
    else:
        form = PatentForm()
    return render(request, 'patents/patent_edit.html', {'form': form})