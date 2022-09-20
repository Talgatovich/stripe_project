import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from items.models import Item
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class ItemsList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "index.html"

    def get(self, request):
        queryset = Item.objects.all()
        return Response({"items": queryset})


class ItemsDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "item_detail.html"

    def get(self, request, id):
        item = get_object_or_404(Item, id=id)
        return Response({"item": item})


class GoToPay(APIView):
    @csrf_exempt
    def get(self, request, id):
        stripe.api_key = settings.STRIPE_PRIVATE_KEY
        item = get_object_or_404(Item, id=id)
        session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price_data": {
                        "currency": "Rub",
                        "product_data": {
                            "name": item.name,
                        },
                        "unit_amount": item.price,
                    },
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url="http://127.0.0.1:8000/",
            cancel_url="http://127.0.0.1:8000/",
        )

        return JsonResponse(
            {
                "session_id": session.id,
                "stripe_pub_key": settings.STRIPE_PUBLIC_KEY,
            }
        )
