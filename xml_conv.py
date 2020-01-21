def read():
    import xml.etree.ElementTree as ET
    tree = ET.parse('accounts.xml')
    root = tree.getroot()
    return root


def to_json():
    import json

    root = read()
    accounts = []
    for account_el in root.iter('account'):
        account = {}
        for field in account_el:
            account[field.tag] = field.text
        accounts.append(account)

    return json.dumps(accounts)


def to_csv():
    import csv

    root = read()
    columns = [
        field.tag
        for field in next(root.iter('account'))
    ]

    accounts = []
    for account_el in root.iter('account'):
        account = {}
        for field in account_el:
            account[field.tag] = field.text
        accounts.append(account)

    
    with open('/tmp/accounts2.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        writer.writerows(accounts)

if __name__=='__main__':
    print(to_json())
    to_csv()