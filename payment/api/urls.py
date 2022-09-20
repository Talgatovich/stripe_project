from django.urls import path

from .views import GoToPay, ItemsDetail, ItemsList

app_name = "api"

urlpatterns = [
    path("items/", ItemsList.as_view(), name="items"),
    path("items/<int:id>/", ItemsDetail.as_view(), name="item_detail"),
    path("buy/<int:id>/", GoToPay.as_view(), name="buy"),
]
