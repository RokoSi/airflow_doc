import json
import logging
from typing import Union, Any, List, Dict

import requests

log = logging.getLogger(__name__)


def count_user_add_menu(url: str, count_user: int = 0):
    """
    Корректно передаеет вводимые данные для добавления пользователя
    :param url:
    :param count_user:

    :return: Ture - если пользователь успешно добавлен,
    False - если не удалось добавить пользователя
    """

    try:
        if count_user == 0:
            count_user = int(input("введите количество пользователей: "))
        json_result: Union[list[dict[Any, Any]], bool] = get_users_url(
            url, count_user
        )
        return json_result


    except TypeError as te:
        print(f"{te}")
        return False
    except ValueError as ve:
        print(f"{ve}")
        print("введите число")


def get_users_url(url: str, count_users: int = 0) -> Union[List[Dict], bool]:
    """
    Получение json с сайта
    :param url:
    :param count_users: количество пользователей
    :return: dict - если удалось получить json файл с сайта,
     bool - если не удалось получить json
    """
    try:
        if url is None:
            log.error("URL для подключения отсутствует в настройках.")
            return False
        else:

            with requests.get(url + str(count_users)) as response:
                if response.status_code == 200:

                    data: Dict = response.json()
                    return data["results"]
                else:
                    return False
    except (requests.exceptions.RequestException, json.decoder.JSONDecodeError) as e:
        log.error(f"Ошибка: {e}")
        return False
    except (KeyError, TypeError) as e:
        log.error(f"Ошибка: {e}")
        return False
