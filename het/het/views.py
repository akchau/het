
from django.shortcuts import redirect
from django.urls import reverse_lazy


def main(request):
    return redirect(reverse_lazy("expenses:list"))
