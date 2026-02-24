import csv

def read_csv_data(file_path):
    with open(file_path, newline='', encoding="utf-8") as csvfile:
        return list(csv.DictReader(csvfile))
