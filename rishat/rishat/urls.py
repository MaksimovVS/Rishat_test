from django.contrib import admin
from django.urls import path

from payment_sys.views import CancelView, SuccessView, CreateSessionView, ItemView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('buy/<pk>/', CreateSessionView.as_view(),
         name='buy'),
    path('item/<pk>/', ItemView.as_view(), name='item')
]
