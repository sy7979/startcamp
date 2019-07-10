import csv

lunch = {
    "BBQ":"123456",
    "중국집":"456789",
    '한식':"7411852"
}

with open("lunch.csv", 'w', encoding="utf-8", newline="") as f:
    csw_writer = csv.writer(f)

    for item in lunch.items():
        csw_writer.writerow(item)