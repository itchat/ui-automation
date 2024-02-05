import csv


class CsvReader:
    """
    非 Wrapper 类型参数
    """

    @classmethod
    def get_data(cls):
        data = []
        with open(r'data\login.csv') as f:
            reader = csv.reader(f, delimiter='\t')
            next(reader)
            for row in reader:
                data.append(row)
        # print(data)
        return data


def csv_data(csv_header, csv_reader):
    def decorator(func):
        def wrapper(self):
            for row in csv_reader.get_data():
                mapped_data = dict(zip(csv_header.split(','), row))
                print(mapped_data)
                func(self, mapped_data)

        return wrapper

    return decorator
