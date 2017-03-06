

def simplify_debt(debts):
    accounts = {}
    for debt in debts:
        if debt.owner not in accounts:
            accounts[debt.owner] = 0
        if debt.debtor not in accounts:
            accounts[debt.debtor] = 0
        accounts[debt.owner] += debt.amount
        accounts[debt.debtor] -= debt.amount
    owner_gains = []
    debtor_debts = []
    for account, amount in accounts.items():
        if amount > 0:
            owner = type('', (), {})()
            owner.name = account
            owner.amount = amount
            owner_gains.append(owner)
        elif amount < 0:
            debtor = type('', (), {})()
            debtor.name = account
            debtor.amount = -amount
            debtor_debts.append(debtor)

    result_debts = []

    for gain in owner_gains[:]:
        for debt in debtor_debts[:]:
            if gain.amount == debt.amount:
                owner_gains.remove(gain)
                debtor_debts.remove(debt)
                _debt = type('', (), {})()
                _debt.owner = gain.name
                _debt.debtor = debt.name
                _debt.amount = debt.amount
                result_debts.append(debt)
                break

    while len(owner_gains) > 0 and len(debtor_debts) > 0:
        sorted(owner_gains, key=lambda x: x.amount)
        highest_gain = owner_gains.pop()

        sorted(debtor_debts, key=lambda x: x.amount)
        highest_debt = debtor_debts.pop()

        _debt = type('', (), {})()
        _debt.owner = highest_gain.name
        _debt.debtor = highest_debt.name
        _debt.amount = min([highest_debt.amount, highest_gain.amount])

        result_debts.append(_debt)

        highest_gain.amount -= _debt.amount
        highest_debt.amount -= _debt.amount

        if highest_debt.amount > 0:
            debtor_debts.append(highest_debt)
        if highest_gain.amount > 0:
            owner_gains.append(highest_gain)

    return result_debts

num_debts = int(raw_input())
debts = []
for i in range(num_debts):
    line = raw_input()
    elem = line.split(' ')
    elem = [value for value in elem if value != ' ' and value != '->']
    debt = type('', (), {})()
    debt.owner = elem[1].upper()
    debt.debtor = elem[0].upper()
    debt.amount = int(elem[2])
    debts.append(debt)

simple_debts = simplify_debt(debts)

for debt in simple_debts:
    print(debt.debtor + ' -> ' + debt.owner + ' ' + str(debt.amount))
