from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('blog/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))
    # 上には古いですviews
    template_name = 'blog/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
 
class DetailView(generic.DetailView):
    # return HttpResponse("You're looking at question" %question_id)
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'blog/detail.html', {'question': question})
    model = Question
    template_name = 'blog/detail.html'

class ResultsView(generic.DetailView):
    # response = "You're lokking at the results of question %s."
    # return HttpResponse(response % question_id)
    model = Question
    template_name = 'blog/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'blog/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('blog:results', args=(question.id,)))