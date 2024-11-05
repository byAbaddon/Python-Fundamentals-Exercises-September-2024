def header():
    print('CASH RECEIPT')


def body():
    print('-' * 30)
    print('Charged to' + '_' * 20)
    print('Received by' + '_' * 19)
    print('-' * 30)


def footer():
    print('\u00A9', 'SoftUni')


def call():
    header()
    body()
    footer()


call()
