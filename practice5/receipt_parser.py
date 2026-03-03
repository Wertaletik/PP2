import re
import json

def parse_receipt(a):
    with open(a, 'r', encoding='utf-8') as f:
        raw = f.read()



    price = r'(\d+,\d{3})\s*x\s*(\d+,\d{2})'
    prices = re.findall(price, raw)
    prices_clean = [
        float((p[1].replace(" ", "")).replace(",", "."))*float((p[0].replace(" ","")).replace(",","."))
        for p in prices
    ]



    product = r'\d+\.\n(.+?)\n\d'
    products = re.findall(product, raw, re.DOTALL)
    products = [p.replace('\n', ' ').strip() for p in products]



    total=list(
        float((q[0].replace(" ", "")).replace(",", "."))
        for q in prices
    )
    total_amount=sum(total)



    datetime = r'Время:\s*(\d{2}\.\d{2}\.\d{4})\s*(\d{2}:\d{2}:\d{2})'
    datetime_match = re.search(datetime, raw)
    date = None
    time = None
    if datetime_match:
        date = datetime_match.group(1)
        time = datetime_match.group(2)



    payment = r'(Банковская карта|Наличные):'
    payment_match = re.search(payment, raw)
    payment_method = payment_match.group(1) if payment_match else None



    result = {
        "products": products,
        "prices": prices_clean,
        "total_amount": total_amount,
        "date": date,
        "time": time,
        "payment_method": payment_method
    }
    return result



data = parse_receipt(r"C:\Study\PP2\practice5\raw.txt")
print(json.dumps(data, indent=2, ensure_ascii=False))