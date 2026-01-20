from bs4 import BeautifulSoup
import os 
from itertools import chain

def get_urls():
    urls = []
    for i in range(1, 51):
       url = f"https://www.hemnet.se/salda/bostader?sold_age=12m&location_ids=898741&page={i}"
       urls.append(url)
    return urls

def scrape():
    contents = []
    for file in os.listdir("soups"):
        content = open(os.path.join("soups", file), encoding="utf-8").read()
        soup = BeautifulSoup(content, 'html.parser')

        name_selector = "div.Header_truncate__ebq7a"
        name = [i.text for i in soup.select(name_selector)]
        
        area_selector = "div.Location_address___eOo4"
        area = [i.text for i in soup.select(area_selector)]

        sold_date_selector = "span.Label_hclLabelSoldAt__gw0aX"
        sold_date = [i.text for i in soup.select(sold_date_selector)]

        price_selector = "div.hcl-flex--container > span.Text_hclText__V01MM "
        price = [i.text for i in soup.select(price_selector)]
        del price[:4]
        price = [
        s.replace('Slutpris', '')
        .replace('\xa0', '')
        .strip()
        for s in price
        if s.startswith('Slutpris')
        ]

        procent = [i.text for i in soup.select(price_selector)]  
        del procent[:4] 
        procent = [
        s.replace('\xa0', '').strip()
        for s in procent
        if '%' in s
        ]   

        square_meter_selector = "div.hcl-flex--container.hcl-flex--gap-2 > p.Text_hclText__V01MM.Text_hclTextMedium__5uIGY"
        square_meter = [i.text for i in soup.select(square_meter_selector)]

        square_meter = [
        s.replace('\xa0', '').replace('m²', '').strip()
        for s in square_meter
        if 'm²' in s
        ]

        rooms_selector = "div.hcl-flex--container.hcl-flex--gap-2 > p.Text_hclText__V01MM.Text_hclTextMedium__5uIGY"
        rooms = [i.text for i in soup.select(rooms_selector)]

        rooms = [
        s.replace('\xa0', '').replace('rum', '').strip()
        for s in rooms
        if 'rum' in s
        ]

        monthly_fee_selector = "div.hcl-flex--container.hcl-flex--gap-2.hcl-flex--justify-space-between.hcl-flex--md-justify-flex-start > span.Text_hclText__V01MM"
        monthly_fee = [i.text for i in soup.select(monthly_fee_selector)]

        monthly_fee = [
            s.replace('\xa0', '').replace('kr/mån', '').strip()
            for s in monthly_fee
            if 'kr/mån' in s
        ]

        price_per_square_meter_selector = "div.SellingPriceAttributes_contentWrapper__VaxX9 > p.Text_hclText__V01MM"
        price_per_square_meter = [i.text for i in soup.select(price_per_square_meter_selector)]

        price_per_square_meter = [
        s.replace('\xa0', '').replace('kr/m²', '').strip()
        for s in price_per_square_meter
        ]
        contents.append([name, area,sold_date,  price,  procent,  square_meter,  rooms,  monthly_fee,  price_per_square_meter])
    contents = [
        list(chain.from_iterable(field_values))
        for field_values in zip(*contents)
    ]
    return contents