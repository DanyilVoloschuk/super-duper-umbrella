from django.urls import path

from inventory_list.views import InventoryList, InventoryView


urlpatterns = [
    path('', InventoryList.as_view()),
    path('item/<pk>', InventoryView.as_view())
]
