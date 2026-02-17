from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

# cria a conexão do seu banco
db = create_engine("sqlite:///database/banco.db")


# cria a base do banco de dados
Base = declarative_base()

# classes/tabelas do banco
# Users:
class Users(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    phone = Column("phone", Integer)
    email = Column("email", String, nullable=False)
    password = Column("password", String)
    active = Column("active", Boolean)
    admin = Column("Admin", Boolean, default=False)

    def __init__(self, name, phone, email, password, active=True, admin=False):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password
        self.active = active
        self.admin = admin
        
# Orders:
class Order(Base):
    __tablename__ = "orders"

    # STATUS_ORDERS = (
    #    ("PENDING", "PENDING"),
    #    ("CANCELED", "CANCELED"),
    #    ("COMPLETED", "COMPLETED")
    # )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String)
    user = Column("user", ForeignKey("users.id"))
    price = Column("price", Float)
    #items =

    def __init__(self, user, status="PENDING", price=0):
        self.user = user
        self.status = status
        self.price = price

        
# OrderItems:
class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantity = Column("quantity", Integer)
    flavor = Column("flavor", String)
    size = Column("size", String)
    unit_price = Column("unit_price", Float)
    order = Column("order", ForeignKey("orders.id"))

    def __init__(self, quantity, flavor, size, unit_price, order):
        self.quantity = quantity
        self.flavor = flavor
        self.size = size
        self.unit_price = unit_price
        self.order = order
        

# executa a criação dos metadados do banco (cria efetivamente o banco de dados)

