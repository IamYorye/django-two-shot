from django.shortcuts import render, redirect, get_object_or_404
from receipts.models import Receipt

# Create your views here.


def receipts_list(request):
    receipts = Receipt.objects.all()
    context = {
        "receipts": receipts,
    }
    return render(request, "receipts/list.html", context)
