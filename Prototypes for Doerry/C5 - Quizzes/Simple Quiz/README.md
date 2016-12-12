# simple-lesson-quiz

A quick and simple Django project example for creating lessons and quizzes. 

## Entities

`simple-lesson-quiz` has three key entities:

1. **Lesson:** Instructional content that forms the basis of a quiz.
2. **Question:** Questions make up the quiz itself and...
    * ...are associated with a lesson.
    * ...are entered by **instructors** via the admin interface.
    * ...can be answered with either a 'Yes' or 'No'.
3. **User Answer:** A record of how a 'student' answered a **Question**.

## User Stories

**A student user** should be able to...
* ...view a list of available lessons.
* ...take the quiz associated with each lesson.

**An instructor user** should be able to...
* ...create lessons (and their associated quizzes) from the admin interface.
* ...see how each 'student' performed on each quiz.

## Installation Instructions

1. Clone down a copy of this repo and navigate inside the outer project folder:

    ```
    $ git clone git@github.com:respondcreate/simple-lesson-quiz.git
    $ cd simple-lesson-quiz/
    ```

2. Create and populate a SQLite database:

    ```
    $ python manage.py migrate
    $ python manage.py loaddata fixture.json
    ```

3. Start up a local webserver:

    ```
    $ python manage.py runserver
    ```

Now visit [http://127.0.0.1:8000/lessons/](http://127.0.0.1:8000/lessons/) to get started!

## Demo Walkthrough

First, make sure your local webserver is running:

```
$ cd simple-lesson-quiz/
$ python manage.py runserver
```

Now visit [http://127.0.0.1:8000/lessons/](http://127.0.0.1:8000/lessons/) in your web browser, it'll redirect you to a login page.

1. Start by logging as a student (the credentials will be right there on the login page). After logging in successfully you'll be greeted with a list of Lessons.
2. To take a lesson, click its associated _Review Lesson Content_ button on the Lesson List page (or, if you're feeling especially smart, skip straight to the quiz by clicking the green _Take Quiz_ button in the right-most column).
3. Once you've read through the lesson you can take its associated quiz by clicking the big green _I'm Ready To Take The Quiz!_ button at the bottom of the Lesson page.
4. Now, answer all the questions on the quiz page and click the green _Submit Answers_ at the bottom. You'll be returned to the Lesson List page after each quiz you complete.

Once you've taken all available quizzes as a student, click 'Logout' at the top of the page and login as an instructor. As an instructor you'll be able to review students' scores or create new lessons & quizzes.
