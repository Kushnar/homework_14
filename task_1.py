# 1.Каждый год ваша компания предоставляет различным
# государственным организациям финансовую отчетность.
# В зависимости от организации форматы отчетности разные. Используя механизм декораторов, решите вопрос
# отчетности для организаций.


def military_report(fun):
    def wrapper():
        print('Military report:')
        a = fun()
        print(f'Tax on military from income: {a["military tax"]}$')

    return wrapper


def tax_office_report(fun):
    def wrapper():
        print('Tax office report:')
        report = fun()
        for i in report:
            if i != 'net profit':
                print(f'{i.capitalize()}: {report.get(i)}$')

    return wrapper


def board_of_directions(fun):
    def wrapper():
        print('Report to board of directions:')
        report = fun()
        for i in report:
            if i == 'military tax':
                print(f'Taxes: {report.get("military tax") + report.get("income tax")}$')
            elif i == 'income tax':
                continue
            else:
                print(f'{i.capitalize()}: {report.get(i)}$')

    return wrapper


@board_of_directions
def report_from_company():
    di = {'income': 200000,
          'salary': 70000,
          'military tax': 7000,
          'income tax': 7000,
          'net profit': 116000}
    return di
