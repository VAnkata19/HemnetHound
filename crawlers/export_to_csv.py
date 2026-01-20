import csv

def export(
    filename,
    name,
    area,
    sold_date,
    price,
    procent,
    square_meter,
    rooms,
    monthly_fee,
    price_per_square_meter
):
    headers = [
        "Name",
        "Area",
        "Sold date",
        "Final price (kr)",
        "Price change (%)",
        "Square meters",
        "Rooms",
        "Monthly fee (kr)",
        "Price per m² (kr)"
    ]

    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)

        for row in zip(
            name,
            area,
            sold_date,
            price,
            procent,
            square_meter,
            rooms,
            monthly_fee,
            price_per_square_meter
        ):
            writer.writerow(row)
