# Cirrus_auto_tests_v1

Команды указываются в консоли 
1. python не ниже версии 3.7.3 (python | узнать версию питона)
2. selenium 3.141.0 | pip install selenium
3. pytest 5.4.3 | pip install pytest
4. перейти в папку с тестами | cd <путь к папке> и выполнить:
-mrdir enviroments
-cd enviroments
-python 3 - venv selenium_env
5. скачать драйвер для соответсвующей версии браузера
6. добавить папку с драйвером C:/chromedriver в корень диска С
7. добавить в переменную path C:/chromedriver
8. для проверки, - что добавилось в консоль, пишется | path 
9. для проверки всех установленный пакетов, - пишется в консоль | pip list

pytest -s -v --domen_name=cirrus2 (#указать нужный домен, имена в конфиге) tests.py (<# название нужного теста)
