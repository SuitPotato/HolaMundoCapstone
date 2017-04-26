# Django Imports
import random

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django import forms
from django.db import models

# Course Management App Imports
from coursemanagement.models import Lesson
from coursemanagement.models import Course
from coursemanagement.forms import LessonForm, CourseForm
from UserSettingsPage.models import Preference
from coursemanagement.models import CourseLessonQuiz, Course, Lesson, Quiz, MultipleChoiceQuiz, MultipleChoiceQuizResponse
from coursemanagement.models import ShortAnswerQuiz, ShortAnswerQuizResponse

# Import User
from django.contrib.auth.models import User

# Create your views here.


# Purpose of the manage is to show all the courses related to the same author
@login_required()
def manage(request):
	#Checks if the user is registered as a Content Creator. If the user is registered as a content
	#creator then they will be able to access this view. If not then they will be redirected to
	#denial page
	if((request.user.groups.filter(name='Content Creator').exists()) or (request.user.is_superuser)):
		# Filters out courses only made by the user
		current_user = request.user
		courses = Course.objects.filter(author=current_user)
		lessons = Lesson.objects.filter(author=current_user)
		context = {"courses": courses, "lessons": lessons}
		return render(request, 'coursemanagement/manage.html', context)
	else:
		return HttpResponseRedirect('/denied/')


# Purpose of viewcourse is to show the lessons specific course.
# Takes in a request and the courseID
# Need to verify if the author is the current user, if not redirect
@login_required()
def viewcourse(request, courseID):
    current_user = request.user
    # Retrieving one value, so no filter needed, but get instead
    # Follows the format (for looking up stuff):
    # field__lookuptype=value
    # courseID__exact = courseID
    course = Course.objects.get(courseID__exact=courseID)
    if (course.author == current_user):

        context = {"course": course}
        return render(request, 'coursemanagement/viewcourse.html', context)
    else:
        # Just a temporary flag
        # Should return a 404
        return render(request, 'mainpage/DragDemo.html')
		

@login_required()
def course(request):
	#Checks if the user is registered as a Content Creator. If the user is registered as a content
	#creator then they will be able to access this view. If not then they will be redirected to
	#denial page
	if((request.user.groups.filter(name='Content Creator').exists()) or (request.user.is_superuser)):
		if request.method == 'POST':
			# form is a variable that contains the courseform
			form = CourseForm(request.POST)
			if form.is_valid():
				# Instantiate the class Course from Models
				v = Course()
				v.title = form.cleaned_data["title"]
				v.description = form.cleaned_data["description"]
				v.difficulty = form.cleaned_data["difficulty"]
				v.author = request.user
				# Must save the instantiated variables afterwards
				v.save()
				# Make sure HttpResponseRedirect has a view and URL
				return HttpResponseRedirect('/success/')
		elif request.method == 'GET':
			form = CourseForm()
		else:
			form = CourseForm()
		return render(request, "coursemanagement/courseform.html", {"form": form})

	#If not a conent creator then redirect to the denial view located in the mainpage
	else:
		return HttpResponseRedirect('/denied/')
		

@login_required()
def success(request):
    return render(request, 'coursemanagement/success.html')


@login_required()
def lesson(request):
	#Checks if the user is registered as a Content Creator. If the user is registered as a content
	#creator then they will be able to access this view. If not then they will be redirected to
	#denial page
	if((request.user.groups.filter(name='Content Creator').exists()) or (request.user.is_superuser)):
		if request.method == 'POST':
			# form is a variable that contains the courseform
			form = LessonForm(request.POST)
			if form.is_valid():
				# Instantiate the class Course from Models
				v = Lesson()
				v.title = form.cleaned_data["title"]
				v.link = form.cleaned_data["link"]
				v.youtube = form.cleaned_data["youtube"]
				v.tabs = form.cleaned_data["tabs"]
				v.tab1desc = form.cleaned_data["tab1desc"]
				v.tab2desc = form.cleaned_data["tab2desc"]
				v.tab3desc = form.cleaned_data["tab3desc"]
				v.tab4desc = form.cleaned_data["tab4desc"]
				v.tab5desc = form.cleaned_data["tab5desc"]
				v.tab6desc = form.cleaned_data["tab6desc"]
				# Must save the instantiated variables afterwards
				v.save()

				# Make sure HttpResponseRedirect has a view and URL
				return HttpResponseRedirect('/success/')
		elif request.method == 'GET':
			form = LessonForm()
		else:
			form = LessonForm()
		return render(request, "coursemanagement/lessonform.html", {"form": form})

	#If not a conent creator then redirect to the denial view located in the mainpage
	else:
		return HttpResponseRedirect('/denied/')

def load_course(request, link, number):
    course = Course.objects.get(link=link)
    allInCourse = CourseLessonQuiz.objects.filter(courseID=course).values()

    try:
        toDisplay = allInCourse[int(number) - 1]
    except:
        return render(request, 'Video_page/404.html')

    if toDisplay["LessonID_id"]:
        video = Lesson.objects.get(lessonID=toDisplay["LessonID_id"])
        context = {'video': video.youtube, 'title': video.title, 'tab1': video.tab1, 'tab2': video.tab2,
                   'tab3': video.tab3, 'tab4': video.tab4, 'tab5': video.tab5, 'tab6': video.tab6,
                   'tab1desc': video.tab1desc, 'tab2desc': video.tab2desc, 'tab3desc': video.tab3desc,
                   'tab4desc': video.tab4desc, 'tab5desc': video.tab5desc, 'tab6desc': video.tab6desc, 'course': link}

        if int(number) == 1:
            context['next'] = 2
        try:
            next = allInCourse[int(number)]
            context['next'] = int(number) + 1
            context['prev'] = int(number) - 1
        except:
            context['prev'] = int(number) - 1
        return render(request, 'coursemanagement/courseloader.html', context)

    elif toDisplay["QuizID_id"]:
        sentence = Quiz.objects.get(quizID=toDisplay["QuizID_id"])
        prevvid = allInCourse[int(number) - 2]
        video = Lesson.objects.get(lessonID=prevvid["LessonID_id"])
        context = {'title': sentence.title, 'wordOne': sentence.wordOne, 'wordTwo': sentence.wordTwo,
                   'wordThree': sentence.wordThree, 'wordFour': sentence.wordFour,
                   'wordFive': sentence.wordFive, 'course': link, 'prevyoutube': video.youtube}

        if int(number) == 1:
            context['next'] = 2
        try:
            next = allInCourse[int(number)]
            context['next'] = int(number) + 1
            context['prev'] = int(number) - 1
        except:
            context['prev'] = int(number) - 1
        return render(request, 'coursemanagement/quizloader.html', context)


        # if request.user.is_authenticated():
        # pref = Preference.objects.get(user=request.user)
        # pref.fourthLastVid = pref.thirdLastVid
        # pref.thirdLastVid = pref.secondLastVid
        # pref.secondLastVid = pref.lastVid

        # pref.save()

        # if toDisplay.QuizID:
        # sentence = toDisplay.QuizID
        # context = {'title': sentence.title, 'wordOne': sentence.wordOne, 'wordTwo': sentence.wordTwo,
        #     'wordThree': sentence.wordThree, 'wordFour': sentence.wordFour,
        #          'wordFive': sentence.wordFive}
        # return render(request, 'DragAndDropQuiz/sentenceTwo.html', context)

    # else:

    return render(request, 'Video_page/404.html')


def quiz_results(request, q, pk):

    # ALL BUT "dd" need to have Quiz db changed to their respective databases
    if q == "ma":
        quiz = Quiz.objects.get(quizID=pk)
        context = {'title': quiz.title, 'score': quiz.score, 'total': quiz.total}
        return render(request, 'coursemanagement/quizresults.html', context)
    elif q == "mc":
        response = MultipleChoiceQuizResponse.objects.get(responseID=pk)
        quiz = MultipleChoiceQuiz.objects.get(quizID=response.quizID.quizID)
        context = {'title': quiz.title, 'score': response.score, 'total': 100}
        return render(request, 'coursemanagement/quizresults.html', context)
    elif q == "dd":
        quiz = Quiz.objects.get(quizID=pk)
        context = {'title': quiz.title, 'score': quiz.score, 'total': quiz.total}
        return render(request, 'coursemanagement/quizresults.html', context)
    elif q == "sa":
        quiz = Quiz.objects.get(quizID=pk)
        context = {'title': quiz.title, 'score': quiz.score, 'total': quiz.total}
        return render(request, 'coursemanagement/quizresults.html', context)
    elif q == "fb":
        quiz = Quiz.objects.get(quizID=pk)
        context = {'title': quiz.title, 'score': quiz.score, 'total': quiz.total}
        return render(request, 'coursemanagement/quizresults.html', context)
    else:
        print("Shouldn't hit")


@login_required()
def create_multiple_choice_quiz(request):
	#Checks if the user is registered as a Content Creator. If the user is registered as a content
	#creator then they will be able to access this view. If not then they will be redirected to
	#denial page
	if((request.user.groups.filter(name='Content Creator').exists()) or (request.user.is_superuser)):
		if request.method == 'POST':
			# if request.POST.get("savebutton") == "Save User info":
			selected_difficulty = request.POST.get("quiz_difficulty")
			selected_number_answers = request.POST.get("question_number")
			return HttpResponseRedirect('/multiplechoice/'+selected_number_answers+'/'+selected_difficulty)
		else:
			number_of_options = MultipleChoiceQuiz.NUMBER_OF_CHOICES
			difficulties = MultipleChoiceQuiz.DIFFICULTIES
			context = {'choices': number_of_options, 'difficulties': difficulties}

			return render(request, 'coursemanagement/multiplechoiceselect.html', context)
	#If not a conent creator then redirect to the denial view located in the mainpage

	else:
		return HttpResponseRedirect('/denied/')

@login_required()
def create_multiple_choice_quiz_q(request, q, d):
	#Checks if the user is registered as a Content Creator. If the user is registered as a content
	#creator then they will be able to access this view. If not then they will be redirected to
	#denial page
    if((request.user.groups.filter(name='Content Creator').exists()) or (request.user.is_superuser)):
		if request.method == 'POST':
			quiz = MultipleChoiceQuiz()
			answers = []
			for i in range(int(q)):
				answers.append(str(request.POST.get(str(int(i)+1)+"-answer")))
			print(answers)
			try:
				quiz.choiceOne = answers[0]
				quiz.choiceTwo = answers[1]
				quiz.choiceThree = answers[2]
				quiz.choiceFour = answers[3]
				quiz.choiceFive = answers[4]
				quiz.choiceSix = answers[5]
			except:
				pass
			quiz.title = request.POST.get("question-answer")
			quiz.author = request.user
			quiz.numberOfChoices = int(q)
			quiz.correctAnswer = quiz.CHOICES[int(request.POST['correct-answer']) - 1][0]
			quiz.difficulty = quiz.DIFFICULTIES[int(d)-1][0]
			quiz.save()

			return HttpResponseRedirect('/success/')
		else:
			questions = MultipleChoiceQuiz.CHOICES

			list_questions = []
			for item in range(int(q)):
				list_questions.append(questions[item])

			print(list_questions)
			context = {'number_questions': list_questions}
			return render(request, 'coursemanagement/multiplechoice.html', context)

	#If not a conent creator then redirect to the denial view located in the mainpage
    else:
		return HttpResponseRedirect('/denied/')

@login_required()
def take_quiz(request, quiz):

    if request.method == 'POST':
        quiz = MultipleChoiceQuiz.objects.get(quizID=quiz)
        response = MultipleChoiceQuizResponse()
        response.user = request.user
        user_answer = request.POST.get('choice')
        print(user_answer)
        print(quiz.correctAnswer)
        response.score = (user_answer == quiz.correctAnswer)
        response.quizID = quiz
        response.save()
        print(response.responseID)
        return HttpResponseRedirect('/quizresults/mc/' + str(response.responseID))
    else:
        quiz = MultipleChoiceQuiz.objects.get(quizID=quiz)
        questions = [quiz.choiceOne, quiz.choiceTwo, quiz.choiceThree, quiz.choiceFour, quiz.choiceFive, quiz.choiceSix]
        questions = [x for x in questions if x is not None]
        print(questions)
        random.shuffle(questions)
        print(questions)
        context = {'title': quiz.title, 'author': quiz.author, 'numChoices': quiz.numberOfChoices, 'questions': questions, 'difficulty': quiz.difficulty}
        return render(request, 'coursemanagement/takemultiplechoicequiz.html', context)
		


def create_fill_in_the_blank(request):
	#Checks if the user is registered as a Content Creator. If the user is registered as a content
	#creator then they will be able to access this view. If not then they will be redirected to
	#denial page
	#if((request.user.groups.filter(name='Content Creator').exists()) or (request.user.is_superuser)):
	
		#FUNCTIONALITY HERE
		
	#If not a conent creator then redirect to the denial view located in the mainpage
	#else:
		#return HttpResponseRedirect('/denied/')
	pass
	
def create_matching(request):
	#Checks if the user is registered as a Content Creator. If the user is registered as a content
	#creator then they will be able to access this view. If not then they will be redirected to
	#denial page
	#if((request.user.groups.filter(name='Content Creator').exists()) or (request.user.is_superuser)):
	
		#FUNCTIONALITY HERE
	
	#If not a conent creator then redirect to the denial view located in the mainpage
	#else:
		#return HttpResponseRedirect('/denied/')
	pass
	
# Short Answer Question Overall Structure
	# Question Prompt
	# Answer 
		
	
def create_short_answer(request):
	#Checks if the user is registered as a Content Creator. If the user is registered as a content
	#creator then they will be able to access this view. If not then they will be redirected to
	#denial page
	if((request.user.groups.filter(name='Content Creator').exists()) or (request.user.is_superuser)):
		if request.method == 'POST':
			quiz = ShortAnswerQuiz()			
			quiz.title = request.POST.get("short-answer-title")
			quiz.author = request.user
			quiz.questionPrompt = request.POST.get("question-area")
			quiz.correctAnswer = request.POST.get("correct-answer")
			quiz.difficulty = request.POST.get("short-answer-difficulty")
			quiz.save()
			
			return HttpResponseRedirect('/success/')
		else:
			return render(request, 'coursemanagement/shortanswer.html')
			
	#If not a conent creator then redirect to the denial view located in the mainpage
	else:
		return HttpResponseRedirect('/denied/')

def take_short_answer(request, id):
	if request.method == 'POST':
		# The actual quiz iteslf being referenced 
		quiz = ShortAnswerQuiz.objects.get(quizID = id)
		# Creating a response model
		response = ShortAnswerQuizResponse()
		# Creating a link to the appropriate quiz
		response.quizID = quiz
		# Grabbing the current session user storing it.
		response.user = request.user
		# Grabbing the correct answer and user answer
		correct_answer = quiz.correctAnswer
		user_answer = request.POST.get("user-input")
		
		# Stripping all spaces and lowering, checking if equal
		if ((user_answer.replace(" ", "")).lower() == (correct_answer.replace(" ", "")).lower() ):
			response.score = 1
		else:
			response.score = 0
		response.save()
		
		# Change to render score redirect later
		return HttpResponseRedirect('/success/')
		
	else:
		quiz = ShortAnswerQuiz.objects.get(quizID = id)
		context = {'title':quiz.title, 'author':quiz.author, 'question':quiz.questionPrompt}
		return render(request, 'coursemanagement/takeshortanswer.html', context)
		
def create_drag_and_drop(request):
	#Checks if the user is registered as a Content Creator. If the user is registered as a content
	#creator then they will be able to access this view. If not then they will be redirected to
	#denial page
	#if((request.user.groups.filter(name='Content Creator').exists()) or (request.user.is_superuser)):
	
		#FUNCTIONALITY HERE
	
	#If not a conent creator then redirect to the denial view located in the mainpage
	#else:
		#return HttpResponseRedirect('/denied/')
	pass