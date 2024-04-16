class CurrencyConverter:
    def __init__(self, usd_to_eur_rate=0.85, eur_to_gbp_rate=0.87, gbp_to_usd_rate=1.29):
        self.usd_to_eur_rate = usd_to_eur_rate
        self.eur_to_gbp_rate = eur_to_gbp_rate
        self.gbp_to_usd_rate = gbp_to_usd_rate

    def usd_to_eur(self, amount):
        return amount * self.usd_to_eur_rate

    def eur_to_gbp(self, amount):
        return amount * self.eur_to_gbp_rate

    def gbp_to_usd(self, amount):
        return amount * self.gbp_to_usd_rate
