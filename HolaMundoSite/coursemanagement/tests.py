from django.test import TestCase
from coursemanagement.models import *

class CoursemanagementTestCase(TestCase):

    def setUp(self):
		Course.objects.create(title="Test Course", description="Test Description", difficulty=2)
        Course.objects.create(title="Course Two", description="Spanish", difficulty=3)
		
		Lesson.objects.create(title="Spanish Lesson", description="Video on dialects", difficulty=1)
		Lesson.objects.create(title="Lesson on Speech", description="Speech lesson", difficulty=3)
		Lesson.objects.create(title="Lesson w/o Quiz", description="Quizless lesson", difficulty=1)
		
		
		MultipleChoiceQuiz.objects.create(LessonID=1, title="Quiz on Spanish Lesson", numberOfChoices=3,
				choiceOne="One", choiceTwo="Two", choiceThree="Three", correctAnswer='C')
		# Correct Answer on Quiz Object below will default to A
		MultipleChoiceQuiz.objects.create(LessonID=2, title="Quiz on Speech", numberOfChoices=2,
				choiceOne="True", choiceTwo="False", correctAnswer='')
				
		CourseLessonQuiz.objects.create(courseID=1, LessonID=1, QuizID=Null, position=1 )
		CourseLessonQuiz.objects.create(courseID=1, LessonID=Null, QuizID=1, position=2 )
		CourseLessonQuiz.objects.create(courseID=2, LessonID=3 ,QuizID=Null, position=1 )
		CourseLessonQuiz.objects.create(courseID=1, LessonID=Null, QuizID=2, position=3 )
		
    def CourseTests(self):
        """Simple Assertions"""
		firstCourseTitle = Course.objects.get(title="Test Course")
		firstCourseDifficulty = Course.objects.get(difficulty=2)
		secondCourseTitle = Course.objects.get(title="Course Two")
		secondCourseDifficulty = Course.objects.get(difficulty=3)
		
	def LessonTests(self):
		firstLessonTitle = Lesson.objects.get(title = "Spanish Lesson")
		firstLessonDifficulty = Lesson.objects.get(difficulty = 1)
		secondLessonTitle = Lesson.objects.get(title = "Lesson on Speech")
		secondLessonDifficulty = Lesson.objects.get(difficulty = 3)
		thirdLessonTitle = Lesson.objects.get(title = "Lesson w/o Quiz")
		thirdLessonDifficulty = Lesson.objects.get(difficulty = 1)
       
	def MultipleChoiceTests(self):
		firstMultChoice = MultipleChoiceQuiz.objects.get(numberOfChoices = 3)
		firstMultAnswer = MultipleChoiceQuiz.objects.get(correctAnswer = 'C')
		secondMultChoice = MultipleChoiceQuiz.objects.get(numberOfChoices = 2)
		secondMultAnswer = MultipleChoiceQuiz.objects.get(correctAnswer = 'A')
		
		