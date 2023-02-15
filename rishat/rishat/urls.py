from django.contrib import admin
from django.urls import path, include

from api.views import CancelView, SuccessView, CreateSessionView, ItemView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('api.urls'))
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('buy/<pk>/', CreateSessionView.as_view(),
         name='buy'),
    path('item/<pk>/', ItemView.as_view(), name='item')
]
