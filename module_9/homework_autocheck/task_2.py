task = """
Реализуйте функцию get_discount_price_customer для расчета цены на товар
интернет-магазина с учетом скидки клиента.
Функция принимает два параметра:
-price — цена продукта
-customer — словарь с данными клиента следующего вида: {"name": "Dima"}
или {"name": "Boris", "discount": 0.15}

У вас есть глобальная переменная DEFAULT_DISCOUNT, которая определяет
скидку для клиента, если у него нет поля discount.
Функция get_discount_price_customer должна возвращать новую цену на
товар для клиента.

Напомним, что дисконт discount — это дробное число от 0 до 1. И мы под
скидкой понимаем коэффициент, который определяет размер от цены. И на
этот размер мы понижаем итоговую цену товара: price = price * (1 - discount).
"""

DEFAULT_DISCOUNT = 0.05


customer = {"name": "Boris", "discount": 0.5}
customer_2 = {"name": "Kiril"}


def get_discount_price_customer(price, customer):
    # discount = customer["discount"] if customer.get(
    #     "discount") or customer.get("discount") == 0 else DEFAULT_DISCOUNT

    # второй вариант
    try:
        discount = customer["discount"]
    except KeyError:
        discount = DEFAULT_DISCOUNT

    return price * (1 - discount)


print(get_discount_price_customer(100, customer))  # 50.0
print(get_discount_price_customer(100, customer_2))  # 95.0
