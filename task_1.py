import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items
    
    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')

        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')

        self.__name_items.append(name)
        self.__number_items += 1

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')

        self.__name_items.remove(name)
        self.__number_items -= 1

    def check_amount(self):
        total = 0

        for item in self.__name_items:
            total += self.__item_price[item]

        if self.__number_items > 10:
            total *= 0.9  

        return total
    
    def twenty_percent_tax_calculation(self):
        total = 0
        for item in self.__name_items:
            if self.__tax_rate[item] == 20:
                total += self.__item_price[item]
        
        if self.__number_items > 10:
            total *= 0.9

        return total * 0.2  

    def ten_percent_tax_calculation(self):
        total = 0
        for item in self.__name_items:
            if self.__tax_rate[item] == 10:
                total += self.__item_price[item]

        if self.__number_items > 10:
            total *= 0.9

        return total * 0.1  


    def total_tax(self):
        total_vat_10 = self.ten_percent_tax_calculation()  
        total_vat_20 = self.twenty_percent_tax_calculation()  
        return total_vat_10 + total_vat_20  
    
    @staticmethod
    def get_telephone_number(telephone_number):
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')

        telephone_str = str(telephone_number)

        if len(telephone_str) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')

        return f'+7{telephone_str}'
    
