import os
import httplib
from argparse import Namespace

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

@login_required()
def index(request):
    form = VidUploadForm()
    return render(request, 'youtube/index.html', {'form': form})


@login_required()
def indexlink(request):
    return render(request, 'youtube/index-link.html')


@login_required()
def uploaded(request):
    if request.method == 'POST':
        form = VidUploadForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            request.description = form.cleaned_data["description"]
            toYoutube(request.FILES['file'], request)

            # change HttpResponse to a page where user can edit information like tags, descriptions, etc
            return HttpResponseRedirect('/results/?query=beginner')
        #else:
            #form = VidUploadForm()
            #return render(request, 'youtube/index.html', {'form': form})


def toYoutube(f, request):
    fs = FileSystemStorage()
    filename = fs.save("Uploaded.mp4", f)
    uploaded_url = fs.url(filename)
    video_abs_path = BASE_URL + uploaded_url

    #Namespace(auth_host_name='localhost', auth_host_port=[8080, 8090],
    #  category='10', description='Test description',
    # file='C:\\Users\\Josh\\Documents\\GitHub\\HolaMundoCapstone\\HolaMundoSite/media/Uploaded_6CXHmaW.mp4',
    #  keywords='', logging_level='ERROR', noauth_local_webserver=False,
    #  privacyStatus='public', title='Test video')

    args = Namespace(auth_host_name='localhost', auth_host_port=[8080, 8090], category='10', description='Test description', file=video_abs_path, keywords='', logging_level='ERROR', noauth_local_webserver=False, privacyStatus='public', title='Test video')
    if not os.path.exists(args.file):
        exit("Please specify a valid file using the --file= parameter.")

    youtube = get_authenticated_service(args)
    try:
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
                    p = Lesson()
                    p.title = response['snippet']['title']
                    p.tags = request.description
                    p.youtube = response['id']
                    p.link = 558
                    p.author = request.user
                    p.save()
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
