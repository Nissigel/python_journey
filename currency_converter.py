def get_amount():
    while True:
        try:
            amount = float(input ('Enter the amount: '))
            if amount <= 0:
                raise ValueError()
            return amount
        except ValueError:
            print ('Invalid amount')

def get_currency(label):
    currencies = ('USD', 'EUR', 'GHS')
    while True:
        currency = input (f'{label} currency (USD/EUR/GHS): ').upper()
        if currency not in currencies:
            print ('Invalid currency')
        else:
            return currency
        
def convert(amount, source_currency, target_currency):
    exchange_rates = {
    'USD':{'EUR': 0.8539, 'GHS': 12.57},
    'EUR':{'USD': 1.171, 'GHS': 14.72},
    'GHS':{'USD': 0.07955, 'EUR': 0.06794},
    }

    if source_currency == target_currency:
        return amount
    
    return amount * exchange_rates[source_currency][target_currency]

def main():
    amount = get_amount()
    source_currency = get_currency('Source')
    target_currency = get_currency('Target')
    converted_amount = convert(amount, source_currency, target_currency)
    print (f'{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}')

if __name__ == '__main__':
    main()