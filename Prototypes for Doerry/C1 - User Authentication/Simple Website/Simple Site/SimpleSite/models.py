from django.db import models
from django.contrib.auth.models import User
from django import forms


##################################User##################################
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password')


##################################List##################################
class List(models.Model):
    title = models.CharField(max_length = 120)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ('title', 'user')


##################################Item##################################
class Item(models.Model):
    title = models.CharField(max_length = 120)
    quantity = models.IntegerField()
    urgency_type = (
        ('1', 'Low'),
        ('2', 'Medium'),
        ('3', 'High'))
    urgency = models.CharField(max_length=1, choices=urgency_type, default='2',
                                    null=True, blank=True)
    category_type = (
        ('1', 'Car'),
        ('2', 'Groceries'),
        ('3', 'Household'))
    category = models.CharField(max_length=1, choices=category_type, default='2',
                                    null=True, blank=True)
    cost = models.IntegerField()
    date = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title

    def geturgency(self):
        category_type = ['Low', 'Medium', 'High']
        return category_type[int(self.category)-1]

    def getcategory(self):
        category_type = ['Car', 'Groceries', 'Household']
        return category_type[int(self.category)-1]

    @property
    def assignees(self):
        return BridgeItemUser.objects.all()

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('title', 'quantity', 'urgency', 'cost', 'category')


##################################Bridge Tables##################################
class BridgeItemList(models.Model):
    item = models.ForeignKey(Item)
    list = models.ForeignKey(List)
    user = models.ForeignKey(User)

class BridgeListUser(models.Model):
    list = models.ForeignKey(List)
    user = models.ForeignKey(User)

class ItemListForm(forms.ModelForm):
    class Meta:
        model = BridgeItemList
        fields = ('item', 'user')

class ListUserForm(forms.ModelForm):
    class Meta:
        model = BridgeListUser
        fields = ('list', 'user')