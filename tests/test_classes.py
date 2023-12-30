from src.classes import Operation


def test_classes():
    operation_1 = Operation("2019-04-04T23:20:05.206878", "Перевод со счета на счет", "Счет 19708645243227258542",
                            "Счет 75651667383060284188", "48223.05", "руб.")
    operation_2 = Operation("2019-04-04T23:20:05.206878", "Перевод со счета на счет", "",
                            "Счет 75651667383060284188", "48223.05", "руб.")
    operation_3 = Operation("2019-04-04T23:20:05.206878", "Перевод со счета на счет", "Maestro 1596837868705199",
                            "Maestro 1596837868705199", "48223.05", "руб.")
    assert operation_1.hide_info_where_from() == 'Счет **8542'
    assert operation_2.hide_info_where_from() == ''
    assert operation_3.hide_info_where_from() == 'Maestro 1596 83** **** 5199'
    assert operation_1.hide_info_to() == 'Счет **4188'
    assert operation_3.hide_info_to() == 'Maestro 1596 83** **** 5199'
    assert operation_2.format_date() == '04.04.2019'
    assert operation_1.print_info() == '2019-04-04T23:20:05.206878 Перевод со счета на счет\nСчет **8542 -> Счет **4188\n48223.05 руб.\n'
    assert operation_1.__repr__() == (
        '2019-04-04T23:20:05.206878 Перевод со счета на счет\nСчет **8542 -> Счет **4188\n48223.05 руб.')
