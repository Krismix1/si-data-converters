def read():
    import csv
    with open('accounts.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            yield tuple(row)


def to_json():
    import json
    reader = read()
    columns = next(reader)
    results = []
    for values in reader:
        row = {}
        for col, val in zip(columns, values):
            row[col] = val
        results.append(row)
    return json.dumps(results)


def to_xml():
    import xml.etree.ElementTree as ET
    reader = read()
    columns = next(reader)
    # create xml
    root = ET.Element('root')
    accounts = ET.SubElement(root, 'accounts')
    for values in reader:
        acc = ET.SubElement(accounts, 'account')
        for index, col in enumerate(columns):
            ET.SubElement(acc, col).text = values[index]
    xmlstr = ET.tostring(root, encoding='utf8', method='xml').decode()
    return xmlstr

if __name__=='__main__':
    print(to_json())
    print()
    print(to_xml())