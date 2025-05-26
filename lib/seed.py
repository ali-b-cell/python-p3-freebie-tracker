from models import Dev, Company, Freebie
from database import session 

from models import engine

session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()
session.commit()

dev1 = Dev(name= "crocs")
dev2 = Dev(name= "Susan")
dev3 = Dev(name= "Santos")

company1 = Company(name="Devs Square", founding_year=2007)
company2 = Company(name="Legicomp", founding_year=2016)
company3 = Company(name="tarakideal", founding_year=2022)

session.add_all([dev1, dev2, dev3, company1, company2, company3])
session.commit()

freebie1 = Freebie(item_name="Cap", value=2, dev=dev1, company=company1)
freebie2 = Freebie(item_name="pen", value=12, dev=dev2, company = company2)
freebie3 =Freebie(item_name="mug", value=6, dev=dev3, company=company1)
freebie4 = Freebie(item_name="Water Bottle", value=2, dev=dev3, company = company2 )

session.add_all([freebie1, freebie2, freebie3, freebie4])
session.commit()

print("Seed added successsfully!")


