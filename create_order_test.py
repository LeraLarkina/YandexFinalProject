# Ларкина Валерия, 16-я когорта — Финальный проект. Инженер по тестированию плюс

from sender_stand_request import post_new_order, get_order
from data import order_body


def test_create_order_get_success_response():
    """
        Тест на успешное создание заказа.
        1. Выполнить запрос на создание заказа.
        2. Сохранить номер трека заказа.
        3. Выполнить запрос на получения заказа по треку заказа.
        4. Проверить, что код ответа равен 200.
    """
    created_order_response = post_new_order(order_body)
    assert created_order_response.status_code == 201

    track = created_order_response.json()["track"]

    order_response = get_order(track)
    assert order_response.status_code == 200
