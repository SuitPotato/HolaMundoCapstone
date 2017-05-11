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
from coursemanagement.models import ShortAnswerQuiz, ShortAnswerQuizResponse, MatchingQuiz

# Import User
from django.contrib.auth.models import User

# Create your views here.


# Purpose of the manage is to show all the courses related to the same author
@login_required()
def manage(request, filter_results='all'):

    # Filters out courses only made by the user
	current_user = request.user
	# Order by Title
	if filter_results == 'title':
		courses = Course.objects.filter(author=current_user).order_by('title')
		context = {"courses":courses}
		return render(request, 'coursemanagement/manage.html', context)
		
	# Order by Title
	elif filter_results == 'creation':
		courses = Course.objects.filter(author=current_user).order_by('-date')
		context = {"courses":courses}
		return render(request, 'coursemanagement/manage.html', context)
		
	# Filter by beginner
	elif filter_results == 'beginner':
		courses = Course.objects.filter(author=current_user).filter(difficulty='1')
		context = {"courses":courses}
		return render(request, 'coursemanagement/manage.html', context)
	
	# Intermediate
	elif filter_results == 'intermediate':
		courses = Course.objects.filter(author=current_user).filter(difficulty='2')
		context = {"courses":courses}
		return render(request, 'coursemanagement/manage.html', context)
	# Advanced
	elif filter_results == 'advanced':
		courses = Course.objects.filter(author=current_user).filter(difficulty='3')
		context = {"courses":courses}
		return render(request, 'coursemanagement/manage.html', context)
	
	else:
		courses = Course.objects.filter(author=current_user)
		#lessons = Lesson.objects.filter(author=current_user)
		context = {"courses": courses}
		return render(request, 'coursemanagement/manage.html', context)
	
	


# Purpose of viewcourse is to show the lessons specific course.
# Takes in a request and the courseID
# Need to verify if the author is the current user, if not redirect
@login_required()
def viewcourse(request, courseID):
    current_user = request.user
    # Need to add lesson
	# Add Quizzes to lesson
	# Try deleting lessons maybe
    course = Course.objects.get(courseID__exact=courseID)
    if (course.author == current_user):
		actualCourseID = course.courseID
		lesson = Lesson.objects.filter(author = current_user).filter(assignedCourse = actualCourseID)
		context = {"course": course, "lessons":lesson}
		return render(request, 'coursemanagement/viewcourse.html', context)
    else:
        # Just a temporary flag
        # Should return a 404
        return render(request, 'mainpage/DragDemo.html')
		


@login_required()
def course(request):
	if((request.user.groups.filter(name='Content Creator').exists()) or (request.user.is_superuser)):
		if request.method == 'POST':
			course = Course()
			relation = CourseLessonQuiz()
			
			course.title = request.POST.get("title")
			course.author = request.user
			course.description = request.POST.get("description")
			course.difficulty = request.POST.get("difficulty")
			course.save()
			
			relation.courseID = course
			relation.save()
			return HttpResponseRedirect('/success/')
		else:
			return render(request, "coursemanagement/createcourse.html")
	else:
		return HttpResponseRedirect('/denied/')

	

@login_required()
def success(request):
    return render(request, 'coursemanagement/success.html')



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


@login_required()
def create_multiple_choice_quiz_q(request, q, d):
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
		


@login_required()

def create_matching_selection(request):

	if request.method == 'POST':
		selected_difficulty = request.POST.get("quiz_difficulty")
		selected_number_options = request.POST.get("question_number")
		return HttpResponseRedirect('/matching/'+selected_difficulty+'/'+selected_number_options)
	else:
		number_of_options = MatchingQuiz.NUMBER_OF_OPTIONS
		difficulty = MatchingQuiz.DIFFICULTIES
		context = {'options': number_of_options, 'difficulty': difficulty}
		return render(request, 'coursemanagement/matchingselect.html', context)
	
	
def create_matching_quiz(request, difficulty, options):
	if request.method == 'POST':

		quiz = MatchingQuiz()
		#quiz.title = request.POST.get("question-title")
		quiz.author = request.user
		quiz.numberOfOptions = int(options)
		quiz.difficulty = int(difficulty)
		
		# Two parts to a matching question. A prompt and the answer to the specific prompt
		prompts = []
		answers = []

		for i in range(int(options)):
			# Adding to the list for prompts and answers, using concatenation to pull the values.
			# Expecting; 1-prompt and 1-answers for all possible options
			prompts.append(str(request.POST.get(str(int(i)+1) + "-prompt")))
			answers.append(str(request.POST.get(str(int(i)+1) + "-answers")))
		# Blatant copy of multiple choice :)
		try:
			quiz.promptOne = prompts[0]
			quiz.promptTwo = prompts[1]
			quiz.promptThree = prompts[2]
			quiz.promptFour = prompts[3]
			quiz.promptFive = prompts[4]
			quiz.promptSix = prompts[5]
			quiz.promptSeven = prompts[6]
			quiz.promptEight = prompts[7]
			quiz.promptNine = prompts[8]
			quiz.promptTen = prompts[9]
			quiz.promptEleven = prompts[10]
			quiz.promptTwelve = prompts[11]
			quiz.promptThirteen = prompts[12]
			quiz.promptFourteen = prompts[13]
			quiz.promptFifteen = prompts[14]
			
		except:
			pass
		try:
			quiz.answerOne = answers[0]
			quiz.answerTwo = answers[1]
			quiz.answerThree = answers[2]
			quiz.answerFour = answers[3]
			quiz.answerFive = answers[4]
			quiz.answerSix = answers[5]
			quiz.answerSeven = answers[6]
			quiz.answerEight = answers[7]
			quiz.answerNine = answers[8]
			quiz.answerTen = answers[9]
			quiz.answerEleven = answers[10]
			quiz.answerTwelve = answers[11]
			quiz.answerThirteen = answers[12]
			quiz.answerFourteen = answers[13]
			quiz.answerFifteen = answers[14]
		except:
			pass
			
		quiz.save()
	else:
		number = MatchingQuiz.NUMBER_OF_OPTIONS
	
		list_prompts = []
		for prompts in range(int(options)):
			list_prompts.append(number[prompts])

		quiz = MatchingQuiz()	
		context = {'options':list_prompts}
		
		return render(request, 'coursemanagement/matching.html', context)
		

# Short Answer Question Overall Structure
	# Question Prompt
	# Answer 
		
	
def create_short_answer(request):
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

# Returns a redirect with difficulty and number of words		
def create_sentence_drag_and_drop(request):
	if request.method == 'POST':
		quiz_difficulty = request.POST.get("quiz_difficulty")
		word_count = request.POST.get("word_count")
		return HttpResponseRedirect('/dragndrop/' + word_count + '/' + quiz_difficulty)
	else:
		return render(request, 'coursemanagement/dragndrop.html')
		

def create_sentence_drag_and_drop_two(request, words, difficulty):
	if request.method == 'POST':
		quiz = DragAndDropQuiz()
		quiz.author = request.author
		# Passing parameters into the values
		quiz.wordCount = int(words)
		quiz.difficulty = int(difficulty)
		wordList = []
		
		for i in range(int(words)):
			# Adding to the list for words, using concatenation to pull the values
			# Expecting" i-word for all of the words
			wordList.append(str(request.POST.get(str(int(i)+1) + "-word")))
		try:
			quiz.wordOne = wordList[0]
			quiz.wordTwo = wordList[1]
			quiz.wordThree = wordList[2]
			quiz.wordFour = wordList[3]
			quiz.wordFive = wordList[4]
			quiz.wordSix = wordList[5]
			quiz.wordSeven = wordList[6]
			quiz.wordEight = wordList[7]
			quiz.wordNine = wordList[8]
			quiz.wordTen = wordList[9]
			quiz.wordEleven = wordList[10]
			quiz.wordTwelve = wordList[11]
			quiz.wordThirteen = wordList[12]
			quiz.wordFourteen = wordList[13]
			quiz.wordFifteen = wordList[14]
		except:
			pass
	else:
		number = DragAndDropQuiz()
		word_List = []
		for x in range(int(words)):
			word_List.append(number[x])
		context = {'words': word_List}
		return render(request, 'coursemanagement/dragndrop.html',context)

# Not a form so no submission		
def take_drag_and_drop(request, quiz):
	quiz = DragAndDropQuiz.objects.get(quizID = quiz)
	wordList = []
	
	for i in range(int(wordCount)):
		wordAppend = "word" + (str(wordCount))
		wordAppend = (WordAppend,i)
		wordList.append(quiz.wordAppend)
	shuffledList = shuffle(wordList)
	context = {'words': shuffledList}
	return render(reuqest, 'coursemanagement/takedragndrop.html', context)

@login_required()
# Pass in the Lesson later along with it later.
def create_quiz(request, courseID):
	course = Course.objects.get(courseID__exact=courseID)
	if request.method == 'POST':
		quiz = response.POST.get("select_quiz")
		if quiz == 1:
			# Short Answer
			return HttpResponseRedirect('/shortanswer/')
		elif quiz == 2:
			# Multiple Choice
			return HttpResponseRedirect('/multiplechoice/')
		elif quiz == 3:
			# Matching
			pass
		elif quiz == 4:
			# Sentence Drag & Drop
			pass
		elif quiz == 5:
			# Video Drag & Drop
			pass
		else:
			context = {"course":course}
			return render(request, "coursemanagement/createquiz.html", context)
	else:
		context = {"course":course}
		return render(request, "coursemanagement/createquiz.html", context)




