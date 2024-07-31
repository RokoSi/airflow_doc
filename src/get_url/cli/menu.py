from typing import Callable, List, Dict

from .check_email import check_email
from .count_user_add_menu import count_user_add_menu
from .delite_user import delite_user
from .exit_program import exit_program
from .invalid_users import invalid_users
from .update_param import update_param
from .valid_user import valid_users


def main_menu(settings):
    """
    Cli для взаимодействия с функционалом.
    :param settings: Данные для подключения к бд.
    """
    menu_elements: List[str] = [
        "1. Добавить пользователей",
        "2. Получить валидных пользователей",
        "3. Получить невалидных пользователей",
        "4. Проверить наличие email",
        "5. Изменение данных",
        "6. Удалить пользователя",
        "7. Выйти",
    ]

    # create_db(settings)

    choices_part_func: Dict[int, Callable] = {
        1: count_user_add_menu,
        2: valid_users,
        3: invalid_users,
        4: check_email,
        5: update_param,
        6: delite_user,
        7: exit_program,
    }

    while True:
        print("Меню:")
        for item in menu_elements:
            print(item)
        try:
            choice: int = int(input("Выберите пункт меню: "))
            if choice in choices_part_func:
                action_menu = choices_part_func[choice]
                if choice != 7:
                    action_menu(settings)
                else:
                    action_menu()
            else:
                print("Выбранная опция не поддерживается")
        except ValueError as ve:
            print(f"{ve}")
            print("введите число")


if __name__ == "__main__":
    pass
