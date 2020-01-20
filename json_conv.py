
def read():
    import json
    with open('accounts.json') as f:
        return json.load(f)


def to_csv():
    accounts = read()
    # assume the structure is the same across all elements
    columns = list(accounts[0].keys()) # keep the order consistent
    rows = [','.join(columns)]
    for acc in accounts:
        row = []
        for col in columns: # read the values in the order of the columns
            row.append(acc[col])
        rows.append(','.join(row))
    return '\r\n'.join(rows)

def to_csv2():
    import csv
    accounts = read()
    # assume the structure is the same across all elements
    columns = list(accounts[0].keys()) # keep the order consistent

    with open('/tmp/accounts.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)

        writer.writeheader()
        writer.writerows(accounts)

def to_xml():
    import xml.etree.ElementTree as ET
    accounts = read()
    columns = list(accounts[0].keys())
    # create xml
    root = ET.Element('root')
    accounts_el = ET.SubElement(root, 'accounts')
    for account in accounts:
        acc_el = ET.SubElement(accounts_el, 'account')
        for col in columns:
            ET.SubElement(acc_el, col).text = account[col]
    xmlstr = ET.tostring(root, encoding='utf8', method='xml').decode()
    return xmlstr

if __name__=='__main__':
    print(to_csv())
    to_csv2()
    print()
    print(to_xml())