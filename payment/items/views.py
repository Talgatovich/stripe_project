# import stripe
# from django.conf import settings
# from django.shortcuts import get_object_or_404, redirect, render

# from .models import Item

# stripe.api_key = settings.STRIPE_PRIVATE_KEY


# def index(request):
#     items = Item.objects.all()
#     context = {"items": items}
#     return render(request, "index.html", context)


# def buy(request, id):
#     item = get_object_or_404(Item, id=id)
#     session = stripe.checkout.Session.create(
#         line_items=[
#             {
#                 "price_data": {
#                     "currency": "Rub",
#                     "product_data": {
#                         "name": item.name,
#                     },
#                     "unit_amount": item.price,
#                 },
#                 "quantity": 1,
#             }
#         ],
#         mode="payment",
#         success_url="http://127.0.0.1:8000/",
#         cancel_url="http://127.0.0.1:8000/",
#     )
#     return redirect(session.url, code=303)
