import json
from src.classes import *
from config import *


def get_user_operations():
    """функция, получающая пять успешных операции пользователя из json файла"""
    with open(OPERATIONS, encoding="utf-8") as file:
        json_user_operations = file.read()
    dict_user_operations = json.loads(json_user_operations)
    user_operations = []
    for i in range(5):
        if dict_user_operations[i]['state'] == 'EXECUTED':
            if 'from' not in dict_user_operations[i].keys():
                dict_user_operations[i]['from'] = ""
            user_operations.append(Operation(dict_user_operations[i]['date'], dict_user_operations[i]['description'],
                                             dict_user_operations[i]['from'], dict_user_operations[i]['to'],
                                             dict_user_operations[i]['operationAmount']['amount'],
                                             dict_user_operations[i]['operationAmount']['currency']['name']))
            i += 1
    return user_operations


def print_user_operations():
    """функция, выводящая пять успешных операций в нужном формате"""
    user_operations = get_user_operations()
    for user_operation in user_operations:
        user_operation.hide_info_where_from()
    for user_operation in user_operations:
        user_operation.hide_info_to()
    for user_operation in user_operations:
        user_operation.format_date()
    for user_operation in user_operations:
        user_operation.print_info()
