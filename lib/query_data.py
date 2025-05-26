from models import Dev, Company, Freebie
from database import session

print("\n---- Deveopers----")
devs = session.query(Dev).all()
for dev in devs:
     print(f"Dev ID: {dev.id}, Name: {dev.name}")

print("\n--- Companies ---")
companies = session.query(Company).all(
)
for company in companies:
     print(f"Company ID: {company.id,} Name: {company.name},Founding Year: {company.founding_year}")

     print("\n--- Freebies ---")
     freebies = session.query(Freebie).all()
     for freebie in freebies:
        print(f"Freebie.ID: {freebie.id}, Item: {freebie.item_name}, Value: {freebie.value}, Dev: {freebie.dev.name}, Company: {freebies.company}")

        session.close()