def get_country_codes(prices):
    c_codes = ""
    new_prices = prices.split()
    for code in new_prices:
        new_code = code[:2]
        c_codes += new_code+", "
    c_codes = c_codes[:-2]    
    return(c_codes)
