from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.template.loader import render_to_string

from .forms import NewQuizForm
from . import forms
from .models import Question, Quiz
from quiz.multichoice.models import MCQuestion
from quiz.multichoice.forms import MCQuestionForm
# Create your views here.


@login_required
def add_quiz(request):
    if request.method == 'POST':
        form = NewQuizForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_quiz = models.Quiz(title=cd['name'],
                                   created_by=request.user
                                   )
            new_quiz.save()
            return HttpResponseRedirect('/home/%d/add' % new_quiz.id)
    else:  # display a form to create a new quiz
        form = forms.NewQuizForm()
    c = RequestContext(request, {'title': '/add/'})
    return render(request, 'quiz/add_quiz.html',
                  {'form': form,
                   'quiz.add_quiz': 'List of Quizzes'},
                  c)


@login_required
def teacher_quizlist(request):
    quizl = Quiz.objects.all().order_by('-created_date')
    return render(request, 'quiz/list_quizzes.html', {'quizlist': quizl})


def question_list(request, quiz_id):
    questions = Question.objects.filter(inquiz_id=quiz_id)
    #quiz = Quiz.objects.filter(quiz_id)
    return render(request, 'quiz/list_questions.html', {'questions': questions, 'quiz_id': quiz_id})

# def question_create(request, quiz_id):
#     data = dict()

#     if request.method == 'POST':
#         form = MCQuestionForm(request.POST)
#         form.inquiz = quiz_id
#         if form.is_valid():
#             form.save()
#             data['form_is_valid'] = True
#             questions = MCQuestion.objects.all()
#             data['html_question_list'] = render_to_string('quiz/partial_question_list.html',
#               {'questions': questions})
#         else:
#             data['form_is_valid'] = False
#     else:
#         form = MCQuestionForm()

#     context = {'form': form}
#     data['html_form'] = render_to_string('quiz/partial_question_create.html',
#         context,
#         request=request,
#     )
#     return JsonResponse(data)


def save_question_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            questions = Question.objects.filter(inquiz_id=quiz_id)
            data['html_question_list'] = render_to_string(
                'quiz/partial_quiz_list.html', {
                    'questions': questions})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context,
                                         request=request)
    return JsonResponse(data)


def question_create(request):
    if request.method == 'POST':
        form = MCQuestionForm(request.POST)
    else:
        form = MCQuestionForm()
    return save_question_form(request, form,
                              'quiz/partial_question_create.html')


def question_update(request, quiz_id, pk):
    book = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = MCQuestionForm(request.POST, instance=book)
    else:
        form = MCQuestionForm(instance=book)
    return save_question_form(request, form,
                              'quiz/partial_book_update.html')


def student_quizlist(request):
    quizl = Quiz.objects.all().order_by('-pk')
    return render(request, 'quiz/student_quiz_list.html', {'quizlist': quizl})


def student_questionlist(request, quiz_id):
    questions = Question.objects.filter(inquiz='quiz_id')
    return render(request, 'quiz/list_questions.html', {'questions': questions})
