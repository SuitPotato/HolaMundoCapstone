from django.contrib import admin
from SimpleSite.models import List, Item, BridgeItemList, BridgeListUser

# Register your models here.
#class SeatsAdmin(admin.ModelSeats):
#	pass
#	admin.site.register(Seats, SeatsAdmin)


admin.site.register(List)
admin.site.register(Item)
admin.site.register(BridgeItemList)
admin.site.register(BridgeListUser)