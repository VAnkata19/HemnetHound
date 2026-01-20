import crawlers

def main():
    # Appends all of the urls
    urls = crawlers.get_urls()

    #calls the function to store all of them
    #crawlers.save_to_html(urls)

    scrape_data = crawlers.scrape()
    crawlers.export(
        filename="hemnet_data.csv",
        name=scrape_data[0],
        area=scrape_data[1],
        sold_date=scrape_data[2],
        price=scrape_data[3],
        procent=scrape_data[4],
        square_meter=scrape_data[5],
        rooms=scrape_data[6],
        monthly_fee=scrape_data[7],
        price_per_square_meter=scrape_data[8]
    )


if __name__ == "__main__":
    main()
