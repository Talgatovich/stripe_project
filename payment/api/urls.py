from django.urls import path

from .views import CancelView, GoToPay, ItemsDetail, ItemsList, SuccessView

app_name = "api"

urlpatterns = [
    path("", ItemsList.as_view(), name="items"),
    path("item/<int:id>/", ItemsDetail.as_view(), name="item_detail"),
    path("buy/<int:id>/", GoToPay.as_view(), name="buy"),
    path("success/", SuccessView.as_view(), name="success"),
    path("cancel/", CancelView.as_view(), name="cancel"),
]
