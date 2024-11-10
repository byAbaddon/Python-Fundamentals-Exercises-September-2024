class BankAccount:
    def __init__(self, ):
        self.Name = ''
        self.Bank = ''
        self.Balance = 0.0
        self.collection = []

    def sort(self):
        sorted_collections = sorted(self.collection, key=lambda x: (-x['balance'], len(x['bank'])))
        for x in sorted_collections:
            print(f"{x['name']} -> {x['balance']:.2f} ({x['bank']})")


account = BankAccount()

for x in [x.split(' | ') for x in iter(input, 'end')]:
    account.Bank, account.Name, account.Balance = x
    account.collection.append({'name': account.Name, 'balance': float(account.Balance), 'bank': account.Bank})

account.sort()

'''
DSK | Ivan | 504.403
DSK | Pesho | 2000.4031
DSK | Aleksander | 20000.0001
Piraeus | Ivan | 504.403
Piraeus | Aleksander | 20000.0001
end
'''
