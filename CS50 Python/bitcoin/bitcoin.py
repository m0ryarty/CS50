import sys
import requests


def main():

    if len(sys.argv) < 2:
        sys.exit('Missing comand-line argument')
    try:
        amount = float(sys.argv[1])
        bitcoin = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
        bitcoin = bitcoin['bpi']['USD']['rate_float']

        dolars = bitcoin * amount

        print(f'${dolars:,}')

    except ValueError:
        sys.exit('Comand-line argument is not a number')
    except requests.RequestException as e:
        print(e)


main()
