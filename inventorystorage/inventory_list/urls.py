from django.urls import path

from inventory_list.views import InventoryList, InventoryView, SetItemToInventory

urlpatterns = [
    path('', InventoryList.as_view()),
    path('item/<int:pk>', InventoryView.as_view()),
    path('add_item_to_user/<int:pk>', SetItemToInventory.as_view())
]
