from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class Students(Base):
    _tablename_ = 'students'  # Adding the table name
    id = Column(Integer, primary_key=True,=True)
    name = Column(String)
    Rollno = Column(String)
    Section = Column(String)
engine = create_engine("sqlite:///mydb.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
s = Session()
s.commit()