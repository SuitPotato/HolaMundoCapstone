#import to give python ability to create functionality for templates
from django import template

#imports group functionality
from django.contrib.auth.models import Group 

#sets variable equal to all of template library functionality
register = template.Library() 

#registers a tag called has_group that can be used in a template
#defines function same as tag that takes in the user and the name of 
#the group
@register.filter(name='has_group') 
def has_group(user, group_name):
	#sets group equal to selected group name from Groups model
    group =  Group.objects.get(name=group_name)
	
	#returns group in template
    return group in user.groups.all() 