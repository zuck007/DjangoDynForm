from django.shortcuts import render, get_object_or_404
from .models import Question, Survey, Response, Answer
from .forms import SurveyForm, ResponseForm, QuestionForm
def index(request):
    all_surveys = Survey.objects.all()
    return render(request, 'dyform/index.html',{'all_surveys':all_surveys})

def create_survey(request):
    created = False
    if request.method == 'POST':
        form = SurveyForm(data=request.POST)
        if form.is_valid():
            created = True
            survey = form.save(commit=False)
            survey.save()
            print("created",created)
            return render(request, 'dyform/create_survey.html', {'form': form, 'created': created, 'survey': survey})
        else:
            print(form.errors)
    else:
        form = SurveyForm()
    return render(request, 'dyform/create_survey.html', {'form': form, 'created': created})

def edit_survey(request, survey_id):
    if request.method == 'POST':
        form = QuestionForm(survey_id=survey_id, data=request.POST, extra=request.POST.get('extra_question_count'))
        if form.is_valid():
            question_form = form.save(commit=False)
            question_form.save()
        else:
            print(form.errors)
    else:
        form = QuestionForm(survey_id=survey_id)    
    return render(request, 'dyform/edit_survey.html', {'form': form})