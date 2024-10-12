import smtplib

MY_EMAIL = "rafalcriscars@gmail.com"
PASSWORD = "igkc mimd srsu eqyx"

car_model = input("Podaj markę i model auta: ")
seller_email_addrs = input("Podaj adres email sprzedawcy: ")

with open("letter1.txt", "r") as file:
    letter_data = file.read()
    new_letter = letter_data.replace("[CAR_MODEL]", car_model)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=seller_email_addrs,
            msg=f"Subject:{car_model}\n\n{new_letter}"
        )