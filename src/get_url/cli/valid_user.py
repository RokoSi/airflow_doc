from typing import Union, List, Dict


def valid_users(settings) -> bool:
    """
    Получение валидных пользователей и их вывод
    :param settings: Данные для подключения к бд
    :return: Ture - если удалось найти таких пользователй,
    False - если не удалось найти таких пользователей
    """
    results: Union[List[Dict], bool] = True  # get_users_db(settings, True)
    if isinstance(results, list):
        if results:
            for row in results:
                print(", ".join(map(str, row)))
            return True
        else:
            print("нет таких записей\n")
            return False
    else:
        print("Ошибка при получении данных")
        return False
