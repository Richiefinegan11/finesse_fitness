from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IAygKLnDo4y5kUjwoqAWihLKyI52bP824tLieC2kaL4LNqw5FsMT6GwluZMjKnvI2A1ss93kSFAok4z3fOF9qzc00ve1WelsT',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
