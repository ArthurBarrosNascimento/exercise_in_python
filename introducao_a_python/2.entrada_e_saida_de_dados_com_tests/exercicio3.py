import json
import csv


def read_json_file(file):
    return json.load(file)


def count_books_by_categories(books):
    categories = {}
    for book in books:
        for category in book['categories']:
            if not categories.get(category):
                categories[category] = 0
            categories[category] += 1
    return categories


def calculate_percentage_by_category(book_count_by_category, total_books):
    return [
        [category, num_books / total_books]
        for category, num_books in book_count_by_category.items()
    ]


def wirte_csv_report(file, header, rows):
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)


if __name__ == '__main__':
    with open('exercicio3.json', 'r') as books_file:
        books = read_json_file(books_file)

    book_count_by_category = count_books_by_categories(books)

    number_of_books = len(books)
    books_percentage_rows = calculate_percentage_by_category(
            book_count_by_category,
            number_of_books
        )

    print(books_percentage_rows)

    header = ['categoria', 'porcetagem']

    with open('report.csv', 'w') as report_file:
        wirte_csv_report(report_file, header, books_percentage_rows)
