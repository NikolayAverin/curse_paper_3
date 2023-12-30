import json
from src.classes import *
from config import *
from operator import itemgetter


def get_user_operations():
    """функция, получающая пять последних успешных операции пользователя из json файла"""
    with open(OPERATIONS, encoding="utf-8") as file:
        json_user_operations = file.read()
    dict_user_operations = json.loads(json_user_operations)
    sort_dict_user_operations = sorted(dict_user_operations, key=itemgetter('date'), reverse=True)
    executed_sort_dict_user_operations = []
    for sort_dict_user_operation in sort_dict_user_operations:
        if sort_dict_user_operation['state'] == 'EXECUTED':
            executed_sort_dict_user_operations.append(sort_dict_user_operation)
    user_operations = []
    for i in range(5):
        if 'from' not in sort_dict_user_operations[i].keys():
            sort_dict_user_operations[i]['from'] = ""
        user_operations.append(
            Operation(sort_dict_user_operations[i]['date'], sort_dict_user_operations[i]['description'],
                      sort_dict_user_operations[i]['from'], sort_dict_user_operations[i]['to'],
                      sort_dict_user_operations[i]['operationAmount']['amount'],
                      sort_dict_user_operations[i]['operationAmount']['currency']['name']))
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
