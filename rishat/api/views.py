import stripe
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from payment_sys.models import Item
from rishat import settings


stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateSessionView(View):
    def get(self, request, *args, **kwargs):
        item_id = self.kwargs["pk"]
        item = Item.objects.get(id=item_id)
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            # paymets_method_types=['card'],
            line_items=[
                {
                    "quantity": 1,
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": item.price,
                        "product_data": {
                            "name": item.name
                        }
                    }
                }
            ],
            metadata={
                "product_id": item.id
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({
            "id": checkout_session.id
        })


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"


class ItemView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        item = Item.objects.get(pk=kwargs['pk'])
        context = {
            "item": item,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        }
        return context


class BuyViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    ...


class ItemViewSet:
    ...
