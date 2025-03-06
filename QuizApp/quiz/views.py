from django.shortcuts import render
from .models import Question, Answer

def quiz_view(request):
    questions = Question.objects.all()
    score = 0
    if request.method == 'POST':
        for question in questions:
            selected_answer = request.POST.get(str(question.id))
            if selected_answer:
                correct_answer = Answer.objects.get(question=question, is_correct=True)
                if selected_answer == str(correct_answer.id):
                    score += 1
        return render(request, 'quiz/result.html', {'score': score, 'total': questions.count()})

    return render(request, 'quiz/quiz.html', {'questions': questions})
