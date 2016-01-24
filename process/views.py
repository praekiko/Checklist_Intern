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

def completedProcess(request, stage_id):
    stage = get_object_or_404(Stage, pk=stage_id)
    try:
        selected_process = stage.process_set.get(pk=request.POST['process'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'process/stageDetail.html', {
            'stage': stage,
            'error_message': "You didn't select a process.",
        })
    else:
        selected_process.isCompleted = True
        selected_process.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('process:reportDetail', args=(stage.id,)))