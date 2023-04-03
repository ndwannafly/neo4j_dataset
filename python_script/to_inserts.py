import csv

FILE_NAME = "../databases/twitter/tweet.csv"
TABLE_NAME = "tweet"


def transform_string(attributes: str, table_name: str) -> str:
    ret = attributes.replace('{', '').replace('}', '");').replace(
        '":', '", "').replace(',"', '", "')
    return 'addVertex("' + table_name + '", ' + ret


table = []
result = []

with open(FILE_NAME) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        table += row

for i in table:
    print(transform_string(i, TABLE_NAME))
