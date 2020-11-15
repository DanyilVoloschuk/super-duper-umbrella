from django.contrib import admin

from inventory_list.models import M2mInventoryToUser, Item, Photo

admin.site.register(M2mInventoryToUser)
admin.site.register(Item)
admin.site.register(Photo)
