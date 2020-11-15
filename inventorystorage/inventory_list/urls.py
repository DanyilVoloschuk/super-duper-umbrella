from django.urls import path

from inventory_list.views import InventoryList


urlpatterns = [
    path('', InventoryList.as_view())
]