from django.shortcuts import render
from django import forms
from .models import Stock
from django.db.models import Q

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = "__all__"

def add_stock_view(request):
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "add.html", context={'form': StockForm()})

def search_view(request):
    header = [
        "Stock Name",
        "Market Price",
        "Quantity"]

    context = {
        'stock': [],
    }
    if request.method == "GET":

        name = request.GET.get('stock')
        price = request.GET.get('price')
        order_by = request.GET.get('order_by') or 'name'

        if name and price:
            stocks = Stock.objects.filter(
                    Q(name__icontains=name) &
                    Q(current_price__gte=float(price))).order_by(order_by)
            if stocks:
                context.update({
                    'name': name,
                    'price': price,
                    'header': header,
                    'stock': [
                        {
                            "name": st.name,
                            "price": st.current_price,
                            "volume": st.volume
                        }
                        for st in stocks
                    ]
                })
    return render(request, "search.html", context=context)