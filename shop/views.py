from django.shortcuts import render


def home(request):
    products = [
        {"name": "Товар 1", "price": 100,
         "description": "10 users included, 2 GB of storage, Email support, Help center access"},
        {"name": "Товар 2", "price": 200,
         "description": "20 users included, 5 GB of storage, Premium support, Help center access"},
        {"name": "Товар 3", "price": 300,
         "description": "30 users included, 10 GB of storage, VIP support, Help center access"},
    ]
    return render(request, 'home.html', {"products": products})


def catalog(request):
    return render(request, 'catalog.html')


def category(request):
    return render(request, 'category.html')


def contacts(request):
    """
    Обрабатывает запросы на страницу 'Контакты'.
    Возвращает страницу с формой обратной связи и контактной информацией.
    """
    # Данные для передачи в шаблон
    contact_info = {
        "email": "support@example.com",
        "phone": "+7 (123) 456-78-90",
        "address": "г. Москва, ул. Примерная, д. 1"
    }

    return render(request, 'contacts.html', {"contact_info": contact_info})
