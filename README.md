# Cirrus_automated_tests_in_python_v2

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

Пример вызова теста: pytest -s -v -m "main" --domen_name=cirrusplatform main_collection_tests.py
Если вы хотите запустить только один какой-то тест, то измените название: @pytest.mark.main на @pytest.mark.test и здесь: pytest -s -v -m "main" --domen_name=cirrusplatform main_collection_tests.py измените main на test. Также обратите внимание на то, что в вызове речь идет о коде, где коллекция создается. Если нужна та же с
секция, то меняйте на: pytest -s -v -m "main" --domen_name=cirrusplatform main_section_tests.py
Флажки можно оставить такие. Либо можно поисктаь новые. Все в ваших руках)
