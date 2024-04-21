### Hexlet tests and linter status:
[![Actions Status](https://github.com/mishablokhin/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/mishablokhin/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/f77e021924c7f230371a/maintainability)](https://codeclimate.com/github/mishablokhin/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/f77e021924c7f230371a/test_coverage)](https://codeclimate.com/github/mishablokhin/python-project-50/test_coverage)

### Описание проекта
Проект **Вычислитель отличий** написан в рамках курса Python-разработчик на Hexlet.
Проект представляет собой консольное приложение, способное находить расхождения в двух JSON или YAML файлах, имеющих плоскую или вложенную структуру данных. 
Приложение поддерживает вывод различий в файлах в консоль в трёх форматах:
1. Stylish
2. Plain
3. JSON

### Работа с приложением
- Установка приложения в систему для текущего пользователя:
```
make package-install
```
- Удаление приложения из системы
```
make package-uninstall
```

- Запуск приложения из терминала после установки:
```
gendiff --format json file1.json file2.json
```
где:
- file1.json, file2.json - путь к файлам с расширением JSON или YAML
- --format - указание формата вывода различий между файлами. Допустимые аргументы: **stylish** (используется по умолчанию), **plain**, **json**.

### Аскинемы с примерами работы программы
asciinema record: run gendiff program
[![asciicast](https://asciinema.org/a/uwRAO40GQtLfb7drCBpUkdXKd.svg)](https://asciinema.org/a/uwRAO40GQtLfb7drCBpUkdXKd)

asciinema record: run gendiff program with two YAML files to compare
[![asciicast](https://asciinema.org/a/PfzYscjRrbpGCKzhpU2qJrKKR.svg)](https://asciinema.org/a/PfzYscjRrbpGCKzhpU2qJrKKR)

asciinema record: run gendiff program with two nested YAML files to compare
[![asciicast](https://asciinema.org/a/90N84DBWnMQMoznzrqeVQqCw5.svg)](https://asciinema.org/a/90N84DBWnMQMoznzrqeVQqCw5)

asciinema record: run gendiff program with plain text output format
[![asciicast](https://asciinema.org/a/a7U2zanFWya4bFHPnURfgyFFU.svg)](https://asciinema.org/a/a7U2zanFWya4bFHPnURfgyFFU)

asciinema record: run gendiff program with JSON output format
[![asciicast](https://asciinema.org/a/EDMfYchEFvYXrpXjsp9XR1YJ0.svg)](https://asciinema.org/a/EDMfYchEFvYXrpXjsp9XR1YJ0)