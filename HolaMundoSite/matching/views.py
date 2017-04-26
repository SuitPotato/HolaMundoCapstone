from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.forms import ModelForm
from django.db import models
from django.contrib.auth.decorators import login_required
from matching.models import *
from matching.forms import *
from django.contrib.auth.models import User
import random

#login required refers to a user having to be logged in to be able to
#access the following content on all functions in the views file
#where it is located
	
#The create matching view takes in a user request. If the request method
#is Post then we call the MatchingForm passing in a request of POST
#We then check if the form is valid and if it is then we call the
#Matching table in the model. We set all the apprpriate fields from
#the model into cleaned data from the user that we then save in the 
#database and return a success page. If the request metod was GET
#then we generate the MatchingForm with no request. The same is
#generated if there request method was neither POST nor GET. We then
#return the rendered creatematching html page with the request and
#the MatchingForm


@login_required()
def create_matching_start(request):
	if request.method == 'POST':
		selected_number_questions = request.POST.get("question_number")
		selected_number_answers = request.POST.get("answer_number")
		return HttpResponseRedirect('/create_matching/'+selected_number_questions+'/'+selected_number_answers)
	else:
		number_of_questions = Matching.NUMBER_OPTIONS
		number_of_choices = Matching.CHOICE_OPTIONS
		context = {'choices': number_of_choices, 'questions': number_of_questions}
		
		return render(request, 'matching/numbermatching.html', context)

'''@login_required()
def create_matching(request, q, d):
	if request.method == 'POST':
		quiz = Matching()
		questions = []
		for i in range(int(q)):
			questions.append(str(request.POST.get(str(int(i)+1)+"-question")))
		try:
			quiz.left_one = questions[0]
			quiz.left_two = questions[1]
			quiz.left_three = questions[2]
			quiz.left_four = questions[3]
			quiz.left_five = questions[4]
			quiz.left_six = questions[5]
			quiz.left_seven = questions[6]
			quiz.left_eight = questions[7]
			quiz.left_nine = questions[8]
			quiz.left_ten = questions[9]
			quiz.left_eleven = questions[10]
			quiz.left_twelve = questions[11]
			quiz.left_thirteen = questions[12]
			quiz.left_fourteen = questions[13]
			quiz.left_fifteen = questions[14]
		except:
			pass
		
		choices = []
		for i in range(int(d)):
			choices.append(str(request.POST.get(str(int(i)+1)+"-choice")))
		try:
			quiz.right_one = choices[0]
			quiz.right_two = choices[1]
			quiz.right_three = choices[2]
			quiz.right_four = choices[3]
			quiz.right_five = choices[4]
			quiz.right_six = choices[5]
			quiz.right_seven = choices[6]
			quiz.right_eight = choices[7]
			quiz.right_nine = choices[8]
			quiz.right_ten = choices[9]
			quiz.right_eleven = choices[10]
			quiz.right_twelve = choices[11]
			quiz.right_thirteen = choices[12]
			quiz.right_fourteen = choices[13]
			quiz.right_fifteen = choices[14]
		except:
			pass
		quiz.author = request.user
		quiz.question_options = int(q)
		quiz.answer_options = int(d)
		quiz.save()
		
		return HttpResponseRedirect('/complete/')
	else:
		context = {'number_questions': q, 'number_choices': d}
		
		return render(request, 'matching/creatematching.html', context)'''
			

@login_required()
def create_matching(request, q, d):
	if request.method == 'POST':
		# Form is a variable that contains the source form
		form = MatchingForm(request.POST)
		if form.is_valid():
			# Specifically calling the model
			v = Matching()
			
			v.title = form.cleaned_data["title"]
			#v.options = form.cleaned_data["options"]
			v.difficulty = form.cleaned_data["difficulty"]
			v.left_one = form.cleaned_data["left_one"]
			v.left_two = form.cleaned_data["left_two"]
			v.left_three = form.cleaned_data["left_three"]
			v.left_four = form.cleaned_data["left_four"]
			v.left_five = form.cleaned_data["left_five"]
			v.left_six = form.cleaned_data["left_six"]
			v.left_seven = form.cleaned_data["left_seven"]
			v.left_eight = form.cleaned_data["left_eight"]
			v.left_nine = form.cleaned_data["left_nine"]
			v.left_ten = form.cleaned_data["left_ten"]
			v.left_eleven = form.cleaned_data["left_eleven"]
			v.left_twelve = form.cleaned_data["left_twelve"]
			v.left_thirteen = form.cleaned_data["left_thirteen"]
			v.left_fourteen = form.cleaned_data["left_fourteen"]
			v.left_fifteen = form.cleaned_data["left_fifteen"]
			
			v.right_one = form.cleaned_data["right_one"]
			v.right_two = form.cleaned_data["right_two"]
			v.right_three = form.cleaned_data["right_three"]
			v.right_four = form.cleaned_data["right_four"]
			v.right_five = form.cleaned_data["right_five"]
			v.right_six = form.cleaned_data["right_six"]
			v.right_seven = form.cleaned_data["right_seven"]
			v.right_eight = form.cleaned_data["right_eight"]
			v.right_nine = form.cleaned_data["right_nine"]
			v.right_ten = form.cleaned_data["right_ten"]
			v.right_eleven = form.cleaned_data["right_eleven"]
			v.right_twelve = form.cleaned_data["right_twelve"]
			v.right_thirteen = form.cleaned_data["right_thirteen"]
			v.right_fourteen = form.cleaned_data["right_fourteen"]
			v.right_fifteen = form.cleaned_data["right_fifteen"]
			
			v.author = request.user
			
			'''string = 0
			if v.right_one != "":
				string += 1
			if v.right_two != "":
				string += 1
			if v.right_three != "":
				string += 1
			if v.right_four != "":
				string += 1
			if v.right_five != "":
				string += 1
			if v.right_six != "":
				string += 1
			if v.right_seven != "":
				string += 1
			if v.right_eight != "":
				string += 1
			if v.right_nine != "":
				string += 1
			if v.right_ten != "":
				string += 1
			if v.right_eleven != "":
				string += 1
			if v.right_twelve != "":
				string += 1
			if v.right_thirteen != "":
				string += 1
			if v.right_fourteen != "":
				string += 1
			if v.right_fifteen != "":
				string += 1
				
			v.string = string'''
			# Must save the variables into the model
			v.save()
			
			# HttpResponseRedirect has a view and URL
			return HttpResponseRedirect('/complete/')
	elif request.method == 'GET':
		form = MatchingForm()
		print("Get Request!")
	else:
		form = MatchingForm()
		print("Else Request!")
	#return render(request, 'matching/creatematching.html', {"form":form})
	context = {'number_questions': q, 'number_choices': d, "form":form}
	print("Return Coming")
	return render(request, 'matching/creatematching.html', context)

#This next view just renders a success html page that lets the user know
#they have succeeded in creating a question

@login_required()
def complete(request):
	return render(request, 'matching/complete.html')

#The view_mathcing view is responsible for the user viewing/answering
#the quiz. It takes in the user request and the quizid for which the
#student is wanting to answer. If the request method is POST then we
#generate the AnswerForm passing in the POST request. We then check if
#the form is valid and if it is 

@login_required()	
def view_matching(request, quizID):
	if request.method == 'POST':
		# Form is a variable that contains the source form
		form = AnswerForm(request.POST)
		
		if form.is_valid():
			m = Matching.objects.get(quizID = quizID) # then get just the one
			# Specifically calling the model
			v = Answer()
			v.answer_one = form.cleaned_data["answer_one"]
			v.answer_two = form.cleaned_data["answer_two"]
			v.answer_three = form.cleaned_data["answer_three"]
			v.answer_four = form.cleaned_data["answer_four"]
			v.answer_five = form.cleaned_data["answer_five"]
			v.answer_six = form.cleaned_data["answer_six"]
			v.answer_seven = form.cleaned_data["answer_seven"]
			v.answer_eight = form.cleaned_data["answer_eight"]
			v.answer_nine = form.cleaned_data["answer_nine"]
			v.answer_ten = form.cleaned_data["answer_ten"]
			v.answer_eleven = form.cleaned_data["answer_eleven"]
			v.answer_twelve = form.cleaned_data["answer_twelve"]
			v.answer_thirteen = form.cleaned_data["answer_thirteen"]
			v.answer_fourteen = form.cleaned_data["answer_fourteen"]
			v.answer_fifteen = form.cleaned_data["answer_fifteen"]
			
			v.left_one = m.left_one
			v.left_two = m.left_two
			v.left_three = m.left_three
			v.left_four = m.left_four
			v.left_five = m.left_five
			v.left_six = m.left_six
			v.left_seven = m.left_seven
			v.left_eight = m.left_eight
			v.left_nine = m.left_nine
			v.left_ten = m.left_ten
			v.left_eleven = m.left_eleven
			v.left_twelve = m.left_twelve
			v.left_thirteen = m.left_thirteen
			v.left_fourteen = m.left_fourteen
			v.left_fifteen = m.left_fifteen
			
			options = int(m.options)
			v.total = options
			'''check = 0
			
			answers = [m.answer0, m.answer1, m.answer2, m.answer3, m.answer4,
			m.answer5, m.answer6, m.answer7, m.answer8, m.answer9, m.answer10,
			m.answer11, m.answer12, m.answer13, m.answer14]
			
			#for x in answers:
				#if x == "":
				#	continue
				#else:
				
			print v.answer_one
			print m.rep5
			print m.answer4
			if m.answer0:
				if v.answer_one == m.rep1:
					v.score += 1
				check += 1
			if m.answer1:
					if v.answer_one == m.rep2:
						v.score += 1
					check += 1
					if v.answer_two == m.rep2:
						v.score += 1
					check += 1
			if m.answer2:
					if v.answer_one == m.rep3:
						v.score += 1
					check += 1
					if v.answer_two == m.rep3:
						v.score += 1
					check += 1
					if v.answer_three == m.rep3:
						v.score += 1
					check += 1
			if m.answer3:
					if v.answer_one == m.rep4:
						v.score += 1
					check += 1
					if v.answer_two == m.rep4:
						v.score += 1
					check += 1
					if v.answer_three == m.rep4:
						v.score += 1
					check += 1
					if v.answer_four == m.rep4:
						v.score += 1
					check += 1
			if m.answer4:
					if v.answer_one == m.rep5:
						v.score += 1
					check += 1
					if v.answer_two == m.rep5:
						v.score += 1
					check += 1
					if v.answer_three == m.rep5:
						v.score += 1
					check += 1
					if v.answer_four == m.rep5:
						v.score += 1
					check += 1
					if v.answer_five == m.rep5:
						v.score += 1
					check += 1
			if m.answer5:
					if v.answer_one == m.rep6:
						v.score += 1
					check += 1
					if v.answer_two == m.rep6:
						v.score += 1
					check += 1
					if v.answer_three == m.rep6:
						v.score += 1
					check += 1
					if v.answer_four == m.rep6:
						v.score += 1
					check += 1
					if v.answer_five == m.rep6:
						v.score += 1
					check += 1
					if v.answer_six == m.rep6:
						v.score += 1
					check += 1
			if m.answer6:
					if v.answer_one == m.rep7:
						v.score += 1
					check += 1
					if v.answer_two == m.rep7:
						v.score += 1
					check += 1
					if v.answer_three == m.rep7:
						v.score += 1
					check += 1
					if v.answer_four == m.rep7:
						v.score += 1
					check += 1
					if v.answer_five == m.rep7:
						v.score += 1
					check += 1
					if v.answer_six == m.rep7:
						v.score += 1
					check += 1
					if v.answer_seven == m.rep7:
						v.score += 1
					check += 1
			if m.answer7:
					if v.answer_one == m.rep8:
						v.score += 1
					check += 1
					if v.answer_two == m.rep8:
						v.score += 1
					check += 1
					if v.answer_three == m.rep8:
						v.score += 1
					check += 1
					if v.answer_four == m.rep8:
						v.score += 1
					check += 1
					if v.answer_five == m.rep8:
						v.score += 1
					check += 1
					if v.answer_six == m.rep8:
						v.score += 1
					check += 1
					if v.answer_seven == m.rep8:
						v.score += 1
					check += 1
					if v.answer_eight == m.rep8:
						v.score += 1
					check += 1
			if m.answer8:
					if v.answer_one == m.rep9:
						v.score += 1
					check += 1
					if v.answer_two == m.rep9:
						v.score += 1
					check += 1
					if v.answer_three == m.rep9:
						v.score += 1
					check += 1
					if v.answer_four == m.rep9:
						v.score += 1
					check += 1
					if v.answer_five == m.rep9:
						v.score += 1
					check 
					if v.answer_six == m.rep9:
						v.score += 1
					check += 1
					if v.answer_seven == m.rep9:
						v.score += 1
					check += 1
					if v.answer_eight == m.rep9:
						v.score += 1
					check += 1
					if v.answer_nine == m.rep9:
						v.score += 1
					check += 1
			if m.answer9:
					if v.answer_one == m.rep10:
						v.score += 1
					check += 1
					if v.answer_two == m.rep10:
						v.score += 1
					check += 1
					if v.answer_three == m.rep10:
						v.score += 1
					check += 1
					if v.answer_four == m.rep10:
						v.score += 1
					check += 1
					if v.answer_five == m.rep10:
						v.score += 1
					check += 1
					if v.answer_six == m.rep10:
						v.score += 1
					check += 1
					if v.answer_seven == m.rep10:
						v.score += 1
					check += 1
					if v.answer_eight == m.rep10:
						v.score += 1
					check += 1
					if v.answer_nine == m.rep10:
						v.score += 1
					check += 1
					if v.answer_ten == m.rep10:
						v.score += 1
					check += 1
			if m.answer10:
					if v.answer_one == m.rep11:
						v.score += 1
					check += 1
					if v.answer_two == m.rep11:
						v.score += 1
					check += 1
					if v.answer_three == m.rep11:
						v.score += 1
					check += 1
					if v.answer_four == m.rep11:
						v.score += 1
					check += 1
					if v.answer_five == m.rep11:
						v.score += 1
					check += 1
					if v.answer_six == m.rep11:
						v.score += 1
					check += 1
					if v.answer_seven == m.rep11:
						v.score += 1
					check += 1
					if v.answer_eight == m.rep11:
						v.score += 1
					check += 1
					if v.answer_nine == m.rep11:
						v.score += 1
					check += 1
					if v.answer_ten == m.rep11:
						v.score += 1
					check += 1
					if v.answer_eleven == m.rep11:
						v.score += 1
					check += 1
			if m.answer11:
					if v.answer_one == m.rep12:
						v.score += 1
					check += 1
					if v.answer_two == m.rep12:
						v.score += 1
					check += 1
					if v.answer_three == m.rep12:
						v.score += 1
					check += 1
					if v.answer_four == m.rep12:
						v.score += 1
					check += 1
					if v.answer_five == m.rep12:
						v.score += 1
					check += 1
					if v.answer_six == m.rep12:
						v.score += 1
					check += 1
					if v.answer_seven == m.rep12:
						v.score += 1
					check += 1
					if v.answer_eight == m.rep12:
						v.score += 1
					check += 1
					if v.answer_nine == m.rep12:
						v.score += 1
					check += 1
					if v.answer_ten == m.rep12:
						v.score += 1
					check += 1
					if v.answer_eleven == m.rep12:
						v.score += 1
					check += 1
					if v.answer_twelve == m.rep12:
						v.score += 1
					check += 1
			if m.answer12:
					if v.answer_one == m.rep13:
						v.score += 1
					check += 1
					if v.answer_two == m.rep13:
						v.score += 1
					check += 1
					if v.answer_three == m.rep13:
						v.score += 1
					check += 1
					if v.answer_four == m.rep13:
						v.score += 1
					check += 1
					if v.answer_five == m.rep13:
						v.score += 1
					check += 1
					if v.answer_six == m.rep13:
						v.score += 1
					check += 1
					if v.answer_seven == m.rep13:
						v.score += 1
					check += 1
					if v.answer_eight == m.rep13:
						v.score += 1
					check += 1
					if v.answer_nine == m.rep13:
						v.score += 1
					check += 1
					if v.answer_ten == m.rep13:
						v.score += 1
					check += 1
					if v.answer_eleven == m.rep13:
						v.score += 1
					check += 1
					if v.answer_twelve == m.rep13:
						v.score += 1
					check += 1
					if v.answer_thirteen == m.rep13:
						v.score += 1
					check += 1
			if m.answer13:
					if v.answer_one == m.rep14:
						v.score += 1
					check += 1
					if v.answer_two == m.rep14:
						v.score += 1
					check += 1
					if v.answer_three == m.rep14:
						v.score += 1
					check += 1
					if v.answer_four == m.rep14:
						v.score += 1
					check += 1
					if v.answer_five == m.rep14:
						v.score += 1
					check += 1
					if v.answer_six == m.rep14:
						v.score += 1
					check += 1
					if v.answer_seven == m.rep14:
						v.score += 1
					check += 1
					if v.answer_eight == m.rep14:
						v.score += 1
					check += 1
					if v.answer_nine == m.rep14:
						v.score += 1
					check += 1
					if v.answer_ten == m.rep14:
						v.score += 1
					check += 1
					if v.answer_eleven == m.rep14:
						v.score += 1
					check += 1
					if v.answer_twelve == m.rep14:
						v.score += 1
					check += 1
					if v.answer_thirteen == m.rep14:
						v.score += 1
					check += 1
					if v.answer_fourteen == m.rep14:
						v.score += 1
					check += 1
			if m.answer14:
					if v.answer_one == m.rep15:
						v.score += 1
					check += 1
					if v.answer_two == m.rep15:
						v.score += 1
					check += 1
					if v.answer_three == m.rep15:
						v.score += 1
					check += 1
					if v.answer_four == m.rep15:
						v.score += 1
					check += 1
					if v.answer_five == m.rep15:
						v.score += 1
					check += 1
					if v.answer_six == m.rep15:
						v.score += 1
					check += 1
					if v.answer_seven == m.rep15:
						v.score += 1
					check += 1
					if v.answer_eight == m.rep15:
						v.score += 1
					check += 1
					if v.answer_nine == m.rep15:
						v.score += 1
					check += 1
					if v.answer_ten == m.rep15:
						v.score += 1
					check += 1
					if v.answer_eleven == m.rep15:
						v.score += 1
					check += 1
					if v.answer_twelve == m.rep15:
						v.score += 1
					check += 1
					if v.answer_thirteen == m.rep15:
						v.score += 1
					check += 1
					if v.answer_fourteen == m.rep15:
						v.score += 1
					check += 1
					if v.answer_fifteen == m.rep15:
						v.score += 1
					check += 1'''
			
			total = 1		
			while(True):
				if(total <= options):
					if(v.answer_one == m.right_one):
						v.score += 1
					total += 1
				else:
					break
				if(total <= options):
					if(v.answer_two == m.right_two):
						v.score += 1
					total += 1
				else:
					break
				if(total <= options):
					if(v.answer_three == m.right_three):
						v.score += 1
					total += 1
				else:
					break
				if(total <= options):
					if(v.answer_four == m.right_four):
						v.score += 1
					total += 1
				else:
					break
				if(total <= options):
					if(v.answer_five == m.right_five):
						v.score += 1
					total += 1
				else:
					break
				if(total <= options):
					if(v.answer_six == m.right_six):
						v.score += 1
					total += 1
				else:
					break
				if(total <= options):
					if(v.answer_seven == m.right_seven):
						v.score += 1
					total += 1
				else:
					break
				if(total <= options):
					if(v.answer_eight == m.right_eight):
						v.score += 1
					total += 1
				else:
					break
				if(total <= options):
					if(v.answer_nine == m.right_nine):
						v.score += 1
					total += 1
				else:
					break
				if(total <= options):
					if(v.answer_ten == m.right_ten):
						v.score += 1
					total += 1
				else:
					break
				if(total <= options):
					if(v.answer_eleven == m.right_eleven):
						v.score += 1
					total += 1
				else:
					break
				if(total <= options):
					if(v.answer_twelve == m.right_twelve):
						v.score += 1
					total += 1
				else:
					break
				if(total <= options):
					if(v.answer_thirteen == m.right_thirteen):
						v.score += 1
					total += 1
				else:
					break
				if(total <= options):
					if(v.answer_fourteen == m.right_fourteen):
						v.score += 1
					total += 1
				else:
					break
				if(total <= options):
					if(v.answer_fifteen == m.right_fifteen):
						v.score += 1
					total += 1
				else:
					break
			v.title = m.title
			v.quizID = m.quizID
			v.user = request.user
			v.save()
			return HttpResponseRedirect('/quizresults/ma/%d' %v.resultsID)
	elif request.method == 'GET':
		form = AnswerForm()
	else:
		form = AnswerForm()
	try:
		matching = Matching.objects.get(quizID = quizID)
		answers = [matching.right_one, matching.right_two, 
		matching.right_three, matching.right_four, matching.right_five,
		matching.right_six, matching.right_seven, matching.right_eight,
		matching.right_nine, matching.right_ten, matching.right_eleven,
		matching.right_twelve, matching.right_thirteen, 
		matching.right_fourteen, matching.right_fifteen]
		random.shuffle(answers)
			
		
		'''matching.answer0 = answers[0]
		matching.answer1 = answers[1]
		matching.answer2 = answers[2]
		matching.answer3 = answers[3]
		matching.answer4 = answers[4]
		matching.answer5 = answers[5]
		matching.answer6 = answers[6]
		matching.answer7 = answers[7]
		matching.answer8 = answers[8]
		matching.answer9 = answers[9]
		matching.answer10 = answers[10]
		matching.answer11 = answers[11]
		matching.answer12 = answers[12]
		matching.answer13 = answers[13]
		matching.answer14 = answers[14]'''
		
		temp = 1
		rep1 = 0
		rep2 = 0
		rep3 = 0
		rep4 = 0
		rep5 = 0
		rep6 = 0
		rep7 = 0
		rep8 = 0
		rep9 = 0
		rep10 = 0
		rep11 = 0
		rep12 = 0
		rep13 = 0
		rep14 = 0
		rep15 = 0
			
		
		
		if answers[0] != "":
			rep1 = temp
			temp += 1
			
		if answers[1] != "":
			rep2 = temp
			temp += 1
		if answers[2] != "":
			rep3 = temp
			temp += 1
		if answers[3] != "":
			rep4 = temp
			temp += 1
		if answers[4] != "":
			rep5 = temp
			temp += 1
		if answers[5] != "":
			rep6 = temp
			temp += 1
		if answers[6] != "":
			rep7 = temp
			temp += 1
		if answers[7] != "":
			rep8 = temp
			temp += 1
		if answers[8] != "":
			rep9 = temp
			temp += 1
		if answers[9] != "":
			rep10 = temp
			temp += 1
		if answers[10] != "":
			rep11 = temp
			temp += 1
		if answers[11] != "":
			rep12 = temp
			temp += 1
		if answers[12] != "":
			rep13 = temp
			temp += 1
		if answers[13] != "":
			rep14 = temp
			temp += 1
		if answers[14] != "":
			rep15 = temp
			temp += 1
			
		#matching.save()
		options = int(matching.options)
	
		context = {'title': matching.title, 'quizID': matching.quizID, 'options': options,
					'left_one': matching.left_one, 'left_two': matching.left_two,
				   'left_three': matching.left_three, 'left_four': matching.left_four,
				   'left_five': matching.left_five, 'left_six': matching.left_six,
				   'left_seven': matching.left_seven, 'left_eight': matching.left_eight,
				   'left_nine': matching.left_nine, 'left_ten': matching.left_ten,
				   'left_eleven': matching.left_eleven, 'left_twelve': matching.left_twelve,
				   'left_thirteen': matching.left_thirteen, 'left_fourteen': matching.left_fourteen,
				   'left_fifteen': matching.left_fifteen,
				   'right_one': answers[0], 'right_two': answers[1],
				   'right_three': answers[2], 'right_four': answers[3],
				   'right_five': answers[4], 'right_six': answers[5],
				   'right_seven': answers[6], 'right_eight': answers[7],
				   'right_nine': answers[8], 'right_ten': answers[9],
				   'right_eleven': answers[10], 'right_twelve': answers[11],
				   'right_thirteen': answers[12], 'right_fourteen': answers[13],
				   'right_fifteen': answers[14], 
				   'rep1': rep1, 'rep2': rep2, 
				   'rep3': rep3, 'rep4': rep4, 'rep5': rep5, 'rep6': rep6,
				   'rep7': rep7, 'rep8': rep8, 'rep9': rep9, 'rep10': rep10,
				   'rep11': rep11, 'rep12': rep12, 'rep13': rep13, 'rep14': rep14,
				   'rep15': rep15, 'form': form}
		return render(request, 'matching/answermatching.html', context)
	except:
		return render(request, 'Video_page/404.html')