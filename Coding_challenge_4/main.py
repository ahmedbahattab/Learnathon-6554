from currency_converter import CurrencyConverter

def main():
    converter = CurrencyConverter()

    # Convert USD to EUR
    usd_amount = 100
    eur_amount = converter.usd_to_eur(usd_amount)
    print(f"{usd_amount} USD is equal to {eur_amount:.2f} EUR")

    # Convert EUR to GBP
    eur_amount = 100
    gbp_amount = converter.eur_to_gbp(eur_amount)
    print(f"{eur_amount} EUR is equal to {gbp_amount:.2f} GBP")

    # Convert GBP to USD
    gbp_amount = 100
    usd_amount = converter.gbp_to_usd(gbp_amount)
    print(f"{gbp_amount} GBP is equal to {usd_amount:.2f} USD")

if __name__ == "__main__":
    main()
