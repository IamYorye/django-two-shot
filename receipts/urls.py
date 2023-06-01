from django.urls import path
from receipts.views import (
    receipts_list,
)

urlpatterns = [
    path("", receipts_list, name="home"),
]
