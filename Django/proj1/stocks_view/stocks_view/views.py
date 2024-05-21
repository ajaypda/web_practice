from django.shortcuts import render


def stock(request):
    stock_info : list[dict] = [
        {
            "name":"ONGC",
            "market_price":279.00,
            "quantity":104,
            "buy_price":274.00,
            "returns":+520.00,
            "url": "https://groww.in/stocks/oil-natural-gas-corporation-ltd",
        },
        {
            "name":"Nippon India ETF Gold BeES",
            "market_price":62.89,
            "quantity":35,
            "buy_price":61.16,
            "returns":+60.55,
            "url":"https://groww.in/etfs/reliance-etf-gold-bees",
        },
        {
            "name":"NIFTYBEES",
            "market_price":249.05,
            "quantity":2,
            "buy_price":236.02,
            "returns":+26.06,
            "url":"https://groww.in/etfs/reliance-etf-nifty-bees",
        },
        {
            "name":"LIQUIDCASE",
            "market_price":102.26,
            "quantity":8,
            "buy_price":101.42,
            "returns":+6.72,
            "url":"https://groww.in/etfs/zerodha-nifty-d-rate-liquid-etf",
        },
        {
            "name":"JUNIORBEES",
            "market_price":720.17,
            "quantity":73,
            "buy_price":692.85,
            "returns":+1994.36,
            "url":"https://groww.in/etfs/reliance-etf-junior-bees",
        },
        {
            "name":"IRFC",
            "market_price":173.25,
            "quantity":22,
            "buy_price":157.00,
            "returns":+357.50,
            "url":"https://groww.in/stocks/indian-railway-finance-corporation-ltd",
        },
        {
            "name":"HDFC Bank",
            "market_price":1466.05,
            "quantity":9,
            "buy_price":1594.75,
            "returns":-1158.30,
            "url":"https://groww.in/stocks/hdfc-bank-ltd",
        },
    ]

    header = [
        "Stock Name",
        "Market Price",
        "Quantity",
        "Buy Price",
        "Returns",
        "Links" ]

    context = {
        'stock': [],
    }

    if request.GET:
        character = request.GET.get("character")
        price = request.GET.get("price")
        if character and price:
            context["character"] = character
            context["price"] = price
            context["header"] = header
            for data in stock_info:
                if character.lower() in data["name"].lower() and float(price) <= data["market_price"]:
                    context["stock"].append(data)

    return render(request, "stocks.html", context)