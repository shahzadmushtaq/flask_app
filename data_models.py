from sqlmodel import SQLModel , Field
from sqlmodel import create_engine , Session , select

class Phones(SQLModel,table=True):
    id : int = Field(primary_key=True)
    title : str  = Field(default="")
    price : int  = Field(default=0)
    currency : str  = Field(default="usd")
    ram : int  = Field(default=0)
    storage : int  = Field(default=0)


# create engine to communicate to database
engine = create_engine("sqlite:///database.db")

#Initialize the table creations
SQLModel.metadata.create_all(engine)
def add_record(phone_id,title,price,currency,ram,storage):
    data_row = Phones(
        id=phone_id,
        title=title,
        price=price,
        currency=currency,
        ram=ram,
        storage=storage
    )
    with Session(engine) as session:
        session.add(data_row)
        session.commit()
    print("Record added to database.")

def get_data_by_id(phone_id):
    data_row = None
    with Session(engine) as session:
        statement = select(Phones).where(Phones.id == phone_id)
        row = session.exec(statement).first()
        data_row=row
    return data_row
def get_all():
    data = None
    with Session(engine) as session:
        statement = select(Phones)
        rows = session.exec(statement).fetchall()
        data=rows
    return data
