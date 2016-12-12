#page rendering and redirecting
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse

#user authentication
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
#cross-site request forgery
from django.template.context_processors import csrf

#models
from SimpleSite.models import UserForm, List, ListForm, BridgeListUser, ListUserForm, Item, ItemForm, BridgeItemList, ItemListForm

def home(request):
    return render(request, 'index.htm', {})

def about(request):
    return render(request, 'about.htm', {})

def register(request):
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            user = User.objects.create_user(request.POST['username'], email=None, password=request.POST['password'])
            user.save()
            return HttpResponseRedirect("../login/")
        else:
            print(form.errors)
    else:
        form = UserForm()
    return render(request,
                    'register.htm',
                    {'form': form})

def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("../lists/")
        else:
            form = UserForm()
            form.username = username
            return render(request, 'login.htm', {'form': form,
                                                 'error': "Invalid login credentials."})
    else:
        form = UserForm()
        return render(request,
                    'login.htm',
                    {'form': form,
                     'error': ""})

@login_required
def userlogout(request):
    logout(request)
    return render(request, "logout.htm")

@login_required
def get_lists(request):
    owned_lists = List.objects.all().filter(user = request.user)
    membered_lists = BridgeListUser.objects.all().filter(user = request.user)
    lists = owned_lists
    form = ListForm()
    return render(request, 'lists.htm', {'lists' : owned_lists, 'membered_lists' : membered_lists, 'form': form})


@login_required
def add_list(request):
    if request.method == 'POST':
        temp = List()
        temp.title = request.POST['title']
        temp.user = request.user
        temp.save()
        print("List saved.")
        return HttpResponseRedirect("../lists/")
    else:
        return HttpResponseRedirect("../lists/")


@login_required
def edit_list(request, list_id):
    list = List.objects.get(pk=list_id)
    form = ListForm(instance=list)
    if request.method == 'POST':
        form = ListForm(data=request.POST, instance=list)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.save()
            print("Item saved.")
            return HttpResponseRedirect("/../lists/")
        else:
            print(form.errors)
    elif request.method == 'GET':
        form = ListForm(instance=list)
        return render(request, 'edit_list.htm', { 'list' : list, 'form' : form, 'errors' : form.errors})
    else:
        return render(request, 'edit_list.htm', { 'list' : list, 'form' : form, 'errors' : form.errors})


@login_required
def remove_list(request, list_id):
    if request.method == 'POST':
        temp = List.objects.get(pk=list_id)
        if request.user == temp.user:
            temp.delete()
        return HttpResponseRedirect("../../lists/")
    else:
        return HttpResponseRedirect("../../lists/")

@login_required
def list_users(request, list_id):
    temp = List.objects.get(pk=list_id)
    bridges = BridgeListUser.objects.all().filter(list = temp)


    form = ListUserForm()
    return render(request, 'users.htm', {'bridges' : bridges, 'list' : temp, 'form' : form})


@login_required
def add_listuser(request, list_id):
    if request.method == 'POST':
        temp = BridgeListUser()
        temp.user = User.objects.get(pk=request.POST['user'])
        temp.list = List.objects.get(pk=list_id)
        temp.save()
        print("User added.")
        return HttpResponseRedirect("/../list_users/" + str(list_id) + "/")
    else:
        return HttpResponseRedirect("/../list_users/" + str(list_id) + "/")


@login_required
def remove_user(request, list_id, bridge_id):
    if request.method == 'POST':
        temp = BridgeListUser.objects.get(pk=bridge_id)
        if request.user == temp.list.user:
            temp.delete()
        return HttpResponseRedirect("/../list_users/" + str(list_id) + "/")
    else:
        return HttpResponseRedirect("/../list_users/" + str(list_id) + "/")

@login_required
def list_items(request, list_id):
    temp = List.objects.get(pk=list_id)
    bridges = BridgeItemList.objects.all().filter(list = temp)

    createform = ItemForm()
    addform = ItemListForm()
    return render(request, 'items.htm', {'bridges' : bridges, 'list' : temp, 'createform' : createform, 'addform' : addform})

@login_required
def create_item(request, list_id):
    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            temp = Item()
            temp.title = request.POST['title']
            temp.quantity = request.POST['quantity']
            temp.urgency = request.POST['urgency']
            temp.cost = request.POST['cost']
            temp.save()
            print("Item saved.")
            return HttpResponseRedirect("/../list_items/" + str(list_id) + "/")
        else:
            print(form.errors)
    else:
        return HttpResponseRedirect("/../list_items/" + str(list_id) + "/")

@login_required
def edit_item(request, list_id, item_id):
    temp = List.objects.get(pk=list_id)
    item = Item.objects.get(pk=item_id)
    form = ItemForm(instance=item)
    if request.method == 'POST':
        form = ItemForm(data=request.POST, instance=item)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.save()
            print("Item saved.")
            return HttpResponseRedirect("/../list_items/" + str(list_id) + "/")
        else:
            print(form.errors)
    elif request.method == 'GET':
        form = ItemForm(instance=item)
        return render(request, 'edit_item.htm', { 'list' : temp, 'form' : form, 'item' : item, 'errors' : form.errors})
    else:
        return render(request, 'edit_item.htm', { 'list' : temp, 'form' : form, 'item' : item, 'errors' : form.errors})

@login_required
def add_item(request, list_id):
    if request.method == 'POST':
        temp = BridgeItemList()
        temp.item = Item.objects.get(pk=request.POST['item'])
        temp.list = List.objects.get(pk=list_id)
        temp.user = User.objects.get(pk=request.POST['user'])
        temp.save()
        print("Item added to list.")
        return HttpResponseRedirect("/../list_items/" + str(list_id) + "/")
    else:
        return HttpResponseRedirect("/../list_items/" + str(list_id) + "/")


@login_required
def remove_item(request, list_id, bridge_id):
    if request.method == 'POST':
        temp = BridgeItemList.objects.get(pk=bridge_id)
        if request.user == temp.list.user:
            temp.delete()
        return HttpResponseRedirect("/../list_items/" + str(list_id) + "/")
    else:
        return HttpResponseRedirect("/../list_items/" + str(list_id) + "/")