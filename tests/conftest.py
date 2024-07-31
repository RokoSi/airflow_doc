import pytest

from src.settings import Settings


@pytest.fixture
def setting_te():
    return Settings(
        host="127.0.0.1",
        db="de_projects",
        user="admin",
        password="password",
        port=5432,
        url="https://randomuser.me/api/?password=special,upper,lower,number",
    )
