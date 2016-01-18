from django.http import Http404
from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from .models import Report, Stage


class IndexView(generic.ListView):
    template_name = 'process/index.html'
    context_object_name = 'latest_report_list'

    def get_queryset(self):
	    """
	    Return the last five published questions (not including those set to be
	    published in the future).
	    """
	    return Report.objects.order_by('-endDate')[:5]

class reportDetail(generic.DetailView):
    model = Report
    template_name = 'process/reportDetail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Report.objects.all()

class stageDetail(generic.DetailView):
    model = Stage
    template_name = 'process/stageDetail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Stage.objects.all()