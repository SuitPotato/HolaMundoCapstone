import os
import httplib
from argparse import Namespace
from urlparse import urlparse, parse_qs

import httplib2
import random
import sys
import time

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from googleapiclient.errors import HttpError
from django.core.files.storage import FileSystemStorage
from .forms import VidUploadForm
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db import models
from .models import *

from coursemanagement.models import Lesson

BASE_URL = settings.MEDIA_ROOT

<<<<<<< HEAD
@login_required()
def index(request):
<<<<<<< HEAD
	#Checks if the user is registered as a Content Creator or super user. If the user is registered as a content
	#creator or super user then they will be able to access this view. If not then they will be redirected to
	#denial page
=======
>>>>>>> origin/pagination
	if((request.user.groups.filter(name='Content Creator').exists()) or (request.user.is_superuser)):
		if request.method == 'POST':
			toYoutube(request.FILES['file'], request)
		else:
			return render(request, 'youtube/index.html')
<<<<<<< HEAD
	
	#If not a conent creator then redirect to the denial view located in the mainpage
=======
>>>>>>> origin/pagination
	else:
		return HttpResponseRedirect('/denied/')

@login_required()
def indexlink(request):
<<<<<<< HEAD
	#Checks if the user is registered as a Content Creator or super user. If the user is registered as a content
	#creator or super user then they will be able to access this view. If not then they will be redirected to
	#denial page
=======
>>>>>>> origin/pagination
	if((request.user.groups.filter(name='Content Creator').exists()) or (request.user.is_superuser)):
		if request.method == 'POST':
			title = request.POST.get("title")
			video_link = request.POST.get("link")
			tags = request.POST.get("tags")

			# Tabs information
			tab1name = request.POST.get("Tab 1-name")
			tab1desc = request.POST.get("Tab 1-desc")

			tab2name = request.POST.get("Tab 2-name")
			tab2desc = request.POST.get("Tab 2-desc")

			tab3name = request.POST.get("Tab 3-name")
			tab3desc = request.POST.get("Tab 3-desc")

			tab4name = request.POST.get("Tab 4-name")
			tab4desc = request.POST.get("Tab 4-desc")

			tab5name = request.POST.get("Tab 5-name")
			tab5desc = request.POST.get("Tab 5-desc")

			tab6name = request.POST.get("Tab 6-name")
			tab6desc = request.POST.get("Tab 6-desc")

			selected_difficulty = request.POST.get("video-difficulty")

			query = urlparse(video_link)
			if query.hostname == 'youtu.be':
				link = query.path[1:]
			if query.hostname in ('www.youtube.com', 'youtube.com'):
				if query.path == '/watch':
					p = parse_qs(query.query)
					link = p['v'][0]
				if query.path[:7] == '/embed/':
					link = query.path.split('/')[2]
				if query.path[:3] == '/v/':
					link = query.path.split('/')[2]
			ourlink = generateLink()

			lesson = Lesson(title=title, youtube=link, author=request.user, link=ourlink, tags=tags,
							difficulty=selected_difficulty,
							tab1=tab1name, tab2=tab2name, tab3=tab3name, tab4=tab4name, tab5=tab5name, tab6=tab6name,
							tab1desc=tab1desc, tab2desc=tab2desc, tab3desc=tab3desc, tab4desc=tab4desc, tab5desc=tab5desc,
							tab6desc=tab6desc
							)
			lesson.save()
			time.sleep(2)
			return HttpResponseRedirect('/video/' + ourlink)
		else:
			context = {'tab_name_length': Lesson._meta.get_field('tab1').max_length, 'tab_desc_length': Lesson._meta.get_field('tab1desc').max_length, 'tabs': ('Tab 1', 'Tab 2', 'Tab 3', 'Tab 4', 'Tab 5', 'Tab 6')}
			return render(request, 'youtube/index-link.html', context)
<<<<<<< HEAD
			
	#If not a conent creator then redirect to the denial view located in the mainpage
=======
>>>>>>> origin/pagination
	else:
		return HttpResponseRedirect('/denied/')
=======
>>>>>>> master


################## Important ##################
####### Do not move client_secrets.json #######
########## From main youtube folder ###########

# Main video upload page
@login_required()
def index(request):
    # Checks if the user is registered as a Content Creator or super user. If the user is registered as a content
    # creator or super user then they will be able to access this view. If not then they will be redirected to
    # denial page
    if ((request.user.groups.filter(name='Content Creator').exists()) or (request.user.is_superuser)):
        # After user uploads video to our site, get the file and upload it to youtube.
        if request.method == 'POST':
            toYoutube(request.FILES['file'], request)
        else:
            # Page loads for first time, GET not POST
            context = {'tabs': ('Tab 1', 'Tab 2', 'Tab 3', 'Tab 4', 'Tab 5', 'Tab 6')}
            return render(request, 'youtube/index.html', context)

    # If not a content creator or super user then redirect to the denial view located in the mainpage
    else:
        return HttpResponseRedirect('/denied/')


@login_required()
def indexlink(request):
    # Checks if the user is registered as a Content Creator or super user. If the user is registered as a content
    # creator or super user then they will be able to access this view. If not then they will be redirected to
    # denial page
    if ((request.user.groups.filter(name='Content Creator').exists()) or (request.user.is_superuser)):
        if request.method == 'POST':

            # Get attributes from form post for video
            title = request.POST.get("title")
            video_link = request.POST.get("link")
            tags = request.POST.get("tags")

            # Tabs information
            tab1name = request.POST.get("Tab 1-name")
            tab1desc = request.POST.get("Tab 1-desc")

            tab2name = request.POST.get("Tab 2-name")
            tab2desc = request.POST.get("Tab 2-desc")

            tab3name = request.POST.get("Tab 3-name")
            tab3desc = request.POST.get("Tab 3-desc")

            tab4name = request.POST.get("Tab 4-name")
            tab4desc = request.POST.get("Tab 4-desc")

            tab5name = request.POST.get("Tab 5-name")
            tab5desc = request.POST.get("Tab 5-desc")

            tab6name = request.POST.get("Tab 6-name")
            tab6desc = request.POST.get("Tab 6-desc")

            difficulties = ("Beginner", "Intermediate", "Advanced")

            selected_difficulty = difficulties[int(request.POST.get("video-difficulty")) - 1]

            # Get youtube video ID from link pasted in
            query = urlparse(video_link)
            if query.hostname == 'youtu.be':
                link = query.path[1:]
            if query.hostname in ('www.youtube.com', 'youtube.com'):
                if query.path == '/watch':
                    p = parse_qs(query.query)
                    link = p['v'][0]
                if query.path[:7] == '/embed/':
                    link = query.path.split('/')[2]
                if query.path[:3] == '/v/':
                    link = query.path.split('/')[2]
            ourlink = generateLink()

            # Build new lesson
            lesson = Lesson(title=title, youtube=link, author=request.user, link=ourlink, tags=tags,
                            difficulty=selected_difficulty,
                            tab1=tab1name, tab2=tab2name, tab3=tab3name, tab4=tab4name, tab5=tab5name, tab6=tab6name,
                            tab1desc=tab1desc, tab2desc=tab2desc, tab3desc=tab3desc, tab4desc=tab4desc,
                            tab5desc=tab5desc,
                            tab6desc=tab6desc
                            )

            # Save lesson to database, wait, redirect user to new video just uploaded.
            lesson.save()
            time.sleep(2)
            return HttpResponseRedirect('/video/' + ourlink)
        # If get, form displays all tab information.
        else:
            # Max length set from database, so if database max length is changed form is too. Don't change these
            context = {'tab_name_length': Lesson._meta.get_field('tab1').max_length,
                       'tab_desc_length': Lesson._meta.get_field('tab1desc').max_length,
                       'tabs': ('Tab 1', 'Tab 2', 'Tab 3', 'Tab 4', 'Tab 5', 'Tab 6')}
            return render(request, 'youtube/index-link.html', context)

    # If not a content creator or super user then redirect to the denial view located in the mainpage
    else:
        return HttpResponseRedirect('/denied/')


def toYoutube(f, request):
    fs = FileSystemStorage()
    filename = fs.save("Uploaded.mp4", f)
    uploaded_url = fs.url(filename)
    video_abs_path = BASE_URL + uploaded_url

    # Namespace(auth_host_name='localhost', auth_host_port=[8080, 8090],
    #  category='10', description='Test description',
    # file='C:\\Users\\Josh\\Documents\\GitHub\\HolaMundoCapstone\\HolaMundoSite/media/Uploaded_6CXHmaW.mp4',
    #  keywords='', logging_level='ERROR', noauth_local_webserver=False,
    #  privacyStatus='public', title='Test video')

    # These args match the youtube API. If in the future youtube api changes, here is where things should be updated
    args = Namespace(auth_host_name='localhost', auth_host_port=[8080, 8090], category='10',
                     description='Test description', file=video_abs_path, keywords='', logging_level='ERROR',
                     noauth_local_webserver=False, privacyStatus='public', title='Test video')
    if not os.path.exists(args.file):
        exit("Please specify a valid file using the --file= parameter.")

    youtube = get_authenticated_service(args)
    try:
        # Uploading to youtube now that API specs are met
        initialize_upload(youtube, args, request)
    except HttpError, e:
        print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

    # os.system('C:/Users/Josh/Documents/GitHub/HolaMundoCapstone/HolaMundoSite/youtube/upload.py --file=' + BASE_URL + uploaded_url + ' --title="Test video" --description="Test description" --category=10 --privacyStatus="public"')
    return HttpResponseRedirect('/youtube/index.html')


# Current Video Category Codes
#
# 1	Film & Animation
# 2	Cars & Vehicles
# 10	Music
# 15	Pets & Animals
# 17	Sports
# 19	Travel & Events
# 20	Gaming
# 22	People & Blogs
# 23	Comedy
# 24	Entertainment
# 25	News & Politics
# 26	How-to & Style
# 27	Education
# 28	Science & Technology
# 29	Non-profits & Activism

# Explicitly tell the underlying HTTP transport library not to retry, since
# we are handling retry logic ourselves.
httplib2.RETRIES = 1

# Maximum number of times to retry before giving up.
MAX_RETRIES = 10

# Always retry when these exceptions are raised.
RETRIABLE_EXCEPTIONS = (httplib2.HttpLib2Error, IOError, httplib.NotConnected,
                        httplib.IncompleteRead, httplib.ImproperConnectionState,
                        httplib.CannotSendRequest, httplib.CannotSendHeader,
                        httplib.ResponseNotReady, httplib.BadStatusLine)

# Always retry when an googleapiclient.errors.HttpError with one of these status
# codes is raised.
RETRIABLE_STATUS_CODES = [500, 502, 503, 504]

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# the {{ Google Cloud Console }} at
# {{ https://cloud.google.com/console }}.
# Please ensure that you have enabled the YouTube Data API for your project.
# For more information about using OAuth2 to access the YouTube Data API, see:
#   https://developers.google.com/youtube/v3/guides/authentication
# For more information about the client_secrets.json file format, see:
#   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
CLIENT_SECRETS_FILE = "\client_secrets.json"

# This OAuth 2.0 access scope allows an application to upload files to the
# authenticated user's YouTube channel, but doesn't allow other types of access.
YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# This variable defines a message to display if the CLIENT_SECRETS_FILE is
# missing.
MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0
To make this sample run you will need to populate the client_secrets.json file
found at:
   %s
with information from the {{ Cloud Console }}
{{ https://cloud.google.com/console }}
For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
""" % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                   CLIENT_SECRETS_FILE))

VALID_PRIVACY_STATUSES = ("public", "private", "unlisted")


def get_authenticated_service(args):
    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
                                   scope=YOUTUBE_UPLOAD_SCOPE,
                                   message=MISSING_CLIENT_SECRETS_MESSAGE)

    storage = Storage("%s-oauth2.json" % sys.argv[0])
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage, args)

    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                 http=credentials.authorize(httplib2.Http()))


def initialize_upload(youtube, options, request):
    tags = None
    if options.keywords:
        tags = options.keywords.split(",")

    body = dict(
        snippet=dict(
            title=options.title,
            description=options.description,
            tags=tags,
            categoryId=options.category
        ),
        status=dict(
            privacyStatus=options.privacyStatus
        )
    )

    # Call the API's videos.insert method to create and upload the video.
    insert_request = youtube.videos().insert(
        part=",".join(body.keys()),
        body=body,
        # The chunksize parameter specifies the size of each chunk of data, in
        # bytes, that will be uploaded at a time. Set a higher value for
        # reliable connections as fewer chunks lead to faster uploads. Set a lower
        # value for better recovery on less reliable connections.
        #
        # Setting "chunksize" equal to -1 in the code below means that the entire
        # file will be uploaded in a single HTTP request. (If the upload fails,
        # it will still be retried where it left off.) This is usually a best
        # practice, but if you're using Python older than 2.6 or if you're
        # running on App Engine, you should set the chunksize to something like
        # 1024 * 1024 (1 megabyte).
        media_body=MediaFileUpload(options.file, chunksize=-1, resumable=True)
    )

    resumable_upload(insert_request, request)


# This method implements an exponential backoff strategy to resume a
# failed upload.
def generateLink():
    chars = "abcdefghijklmnopqrstuvwxyz0123456789";
    while True:
        value = "".join(random.choice(chars) for c in range(10))
        try:
            duplicate_key_video = Lesson.objects.get(link=value)
            value = "".join(random.choice(chars) for c in range(10))
        except:
            return value


def resumable_upload(insert_request, request):
    response = None
    error = None
    retry = 0
    while response is None:
        try:
            print "Uploading file..."
            status, response = insert_request.next_chunk()
            if response is not None:
                if 'id' in response:
                    print "Video id '%s' was successfully uploaded." % response['id']
                    # response is return from youtube api. If we hit here, video successfully uploaded
                    # Now we create a new video, p, and set all of our attributes accordingly
                    p = Lesson()
                    p.title = request.POST.get("title")
                    p.tags = request.POST.get("tags")
                    p.difficulty = request.POST.get("video-difficulty")
                    # response['id'] = youtube video unique identifier
                    p.youtube = response['id']
                    # Generate unique link for our sites use for video
                    p.link = generateLink()
                    p.author = request.user
                    # Save video, wait, direct user to newly uploaded video


                    # Tabs information
                    p.tab1 = request.POST.get("Tab 1-name")
                    p.tab1desc = request.POST.get("Tab 1-desc")

                    p.tab2 = request.POST.get("Tab 2-name")
                    p.tab2desc = request.POST.get("Tab 2-desc")

                    p.tab3 = request.POST.get("Tab 3-name")
                    p.tab3desc = request.POST.get("Tab 3-desc")

                    p.tab4 = request.POST.get("Tab 4-name")
                    p.tab4desc = request.POST.get("Tab 4-desc")

                    p.tab5 = request.POST.get("Tab 5-name")
                    p.tab5desc = request.POST.get("Tab 5-desc")

                    p.tab6 = request.POST.get("Tab 6-name")
                    p.tab6desc = request.POST.get("Tab 6-desc")
                    p.save()
                    time.sleep(2)
                    return HttpResponseRedirect('/video/' + p.link)
                else:
                    exit("The upload failed with an unexpected response: %s" % response)
        except HttpError, e:
            if e.resp.status in RETRIABLE_STATUS_CODES:
                error = "A retriable HTTP error %d occurred:\n%s" % (e.resp.status,
                                                                     e.content)
            else:
                raise
        except RETRIABLE_EXCEPTIONS, e:
            error = "A retriable error occurred: %s" % e

        if error is not None:
            print error
            retry += 1
            if retry > MAX_RETRIES:
                exit("No longer attempting to retry.")

            max_sleep = 2 ** retry
            sleep_seconds = random.random() * max_sleep
            print "Sleeping %f seconds and then retrying..." % sleep_seconds
            time.sleep(sleep_seconds)


if __name__ == '__main__':
    argparser.add_argument("--file", required=True, help="Video file to upload")
    argparser.add_argument("--title", help="Video title", default="Test Title")
    argparser.add_argument("--description", help="Video description",
                           default="Test Description")
    argparser.add_argument("--category", default="22",
                           help="Numeric video category. " +
                                "See https://developers.google.com/youtube/v3/docs/videoCategories/list")
    argparser.add_argument("--keywords", help="Video keywords, comma separated",
                           default="")
    argparser.add_argument("--privacyStatus", choices=VALID_PRIVACY_STATUSES,
                           default=VALID_PRIVACY_STATUSES[0], help="Video privacy status.")
    args = argparser.parse_args()

    if not os.path.exists(args.file):
        exit("Please specify a valid file using the --file= parameter.")

    youtube = get_authenticated_service(args)
    try:
        initialize_upload(youtube, args)
    except HttpError, e:
        print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)