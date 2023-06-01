from django.urls import path
from receipts.views import receipts_list, create_receipt

urlpatterns = [
    path("", receipts_list, name="home"),
    path("create/", create_receipt, name="create_receipt"),
]
