import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        o = r.json()
    except requests.RequestException:
        pass
    k = o["bpi"]
    value = k["USD"]
    bit = value["rate_float"]

    final = float(sys.argv[1]) * bit
    print(f"${final:,.4f}")


main()
