# -*- coding: utf-8 -*-
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_files = [filename.lower() for filename in os.listdir(BASE_DIR)]

files_list = ['program.py', 'readme.md']

def test_program():
    for filename in files_list:
        assert filename in dir_files, "Файл {filename} не найден в корне репозитория"
    try:
        import program
    except Exception as e:
        assert "Не удалось запустить program.py.\n Исправьте в нем ошибки:\n {e}"