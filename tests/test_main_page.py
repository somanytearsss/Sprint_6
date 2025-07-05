import pytest
import allure
from src.pages.main_page import MainPage


@pytest.mark.parametrize("test_case", [
    {
        "title": "Проверка ответа на вопрос: сколько стоит?",
        "locator_method": "get_how_much_locators",
    },
    {
        "title": "Проверка ответа на вопрос: хочу несколько самокатов?",
        "locator_method": "get_multiple_scooters_locators",
    },
    {
        "title": "Проверка ответа на вопрос: как считается время аренды?",
        "locator_method": "get_rental_time_calculated_locators",
    },
    {
        "title": "Проверка ответа на вопрос: можно заказать самокат на сегодня?",
        "locator_method": "get_order_scooter_today_locators",
    },
    {
        "title": "Проверка ответа на вопрос: можно продлить самокат?",
        "locator_method": "get_extend_order_locators",
    },
    {
        "title": "Проверка ответа на вопрос: вы привозите зарядку с самокатом?",
        "locator_method": "get_charging_for_a_scooter_locators",
    },
    {
        "title": "Проверка ответа на вопрос: можно отменить заказ?",
        "locator_method": "get_cancel_the_order_locators",
    },
    {
        "title": "Проверка ответа на вопрос: привозите за МКАД?",
        "locator_method": "get_i_live_across_the_mkad_locators",
    },
])
def test_check_text_important_questions(driver, test_case):
    main_page = MainPage(driver)

    # Используем метод из параметров
    question_locator, answer_locator, expected_answer = getattr(main_page, test_case["locator_method"])()

    # Используем Allure для названия теста
    with allure.step(test_case["title"]):
        main_page.verify_question_answer(question_locator, answer_locator, expected_answer)
        