from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev

if __name__ == '__main__':
     engine = create_engine('sqlite:///freebies.db')
     Session = sessionmaker(bind=engine)
     session = Session()

import ipdb; ipdb.set_trace()

companies = session.query(Company).all()
print(companies)

     #!/usr/bin/env python3


