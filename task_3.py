import json


def sort_by_key(lst):
    try:
        return lst['date']
    except KeyError:
        return '0'


def card_number_masked(n):
    return n[:4] + ' ' + n[5:7] + '** **** ' + n[-4:]


def account_number_masked(n):
    return '**' + n[-4:]


with open('operations.json', 'r') as f:
    data = json.load(f)
    s_data = sorted(data, key=sort_by_key, reverse=True)
    s_data.pop()
    executed_operations = []
    for i in s_data:
        if i.get('state') == 'EXECUTED':
            executed_operations.append(i)
    for i in executed_operations[0:5]:
        date = i.get('date')[0:10].replace('-', '.')
        date_object = f"{date[-2:]}.{date[-5:-3]}.{date[:4]}"
        print(f"{date_object} {i.get('description')}")
        try:
            if 'Счет' in i.get('from'):
                from_number = 'Счет ' + account_number_masked(i.get('from')[5:])
            else:
                from_number = i.get('from')[:-16] + card_number_masked(i.get('from')[-16:])
            if 'Счет' in i.get('to'):
                to_number = 'Счет ' + account_number_masked(i.get('to')[5:])
            else:
                to_number = i.get('to')[:-16] + card_number_masked(i.get('to')[-16:])
        except TypeError:
            to_number = 'Счет ' + account_number_masked(i.get('to')[5:])
            print(f'{to_number}')
        else:
            print(f"{from_number} -> {to_number}")
        print(f"{i.get('operationAmount').get('amount')} {i.get('operationAmount').get('currency').get('name')}")
        print('')
