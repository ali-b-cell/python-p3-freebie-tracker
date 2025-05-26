
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

from sqlalchemy import create_engine
engine = create_engine('sqlite:///freebies.db')
Base = declarative_base()

class Company(Base):
  __tablename__="companies"
  id = Column(Integer, primary_key=True)
  name = Column(String)
  founding_year = Column(Integer)

  company_freebies = relationship("Freebie", back_populates="company")

  def __repr__(self):
    return f"<Company(id={self.id}, name='{self.name}')>"
  
class Dev(Base):
    __tablename__= "devs"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    dev_freebies = relationship("Freebie", back_populates="dev")

    def __repr__(self):
      return f"<Dev(id={self.id}, name='{self.name}')>"
    
class Freebie(Base):
      __tablename__ = "freebies" 
      id = Column(Integer, primary_key=True)
      item_name = Column(String)
      value = Column(Integer)
      dev_id = Column(Integer, ForeignKey('devs.id'))
      company_id = Column(Integer, ForeignKey('companies.id'))



      def __repr__(self):
        return (f"<Freebies(id={self.id}, item_name='{self.item_name}',"
        f"value={self.value}, dev_id={self.dev_id}, company_id={self.company_id}>")
      

      dev = relationship("Dev", back_populates="dev_freebies")
      company = relationship("Company", back_populates="company_freebies")







    


