from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

# Replace with your actual database connection details
connection_string = "mysql+mysqldb://{}:{}@{}/{}".format(
             getenv("USER"),
                getenv("PWD"),
                getenv("HOST"),
                getenv("DB"),
            )
engine = create_engine(connection_string, pool_pre_ping=True,)

# Define base class for table models
Base = declarative_base()

# Define table models reflecting your database schema (modify data types and relationships as needed)
class Region(Base):
    __tablename__ = "Region"

    regionId = Column(Integer, primary_key=True)
    regionName = Column(String(50))

class Branch(Base):
    __tablename__ = "Branch"

    branchId = Column(Integer, primary_key=True)
    branchName = Column(String(50))
    regionId = Column(Integer, ForeignKey(Region.regionId))

class ATM(Base):
    __tablename__ = "ATM"

    atmId = Column(Integer, primary_key=True)
    atmName = Column(String(45))
    networkAddress = Column(String(45))
    latitude = Column(Float)
    longitude = Column(Float)
    timezone = Column(String(45))
    subnet = Column(String(45))
    branchId = Column(Integer, ForeignKey(Branch.branchId))
    groupId = Column(Integer)

    branch = relationship("Branch", backref="atms")
    group = relationship("Group", backref="atms")

class Device(Base):
    __tablename__ = "Device"

    deviceId = Column(Integer, primary_key=True)
    deviceName = Column(String(100))

class AtmDevice(Base):
    __tablename__ = "AtmDevice"

    atmId = Column(Integer, ForeignKey(ATM.atmId), primary_key=True)
    deviceId = Column(Integer, ForeignKey(Device.deviceId), primary_key=True)
    deviceStatus = Column(String(100))

    atm = relationship("ATM", backref="atm_devices")
    device = relationship("Device", backref="atm_devices")

class ElectronicJournal(Base):
    __tablename__ = "ElectronicJournal"

    ejId = Column(Integer, primary_key=True)
    ejData = Column(String(1000))
    atmId = Column(Integer, ForeignKey(ATM.atmId))

class Event(Base):
    __tablename__ = "Event"

    eventId = Column(Integer, primary_key=True)
    eventType = Column(String(100))
    ejId = Column(Integer, ForeignKey(ElectronicJournal.ejId))

class Group(Base):
    __tablename__ = "Group"

    groupId = Column(Integer, primary_key=True)
    groupName = Column(String(100))
    groupDescription = Column(String(100))
    groupType = Column(String(45))
    regionId = Column(Integer, ForeignKey(Region.regionId))

class Transaction(Base):
    __tablename__ = "Transaction"

    transactionId = Column(Integer, primary_key=True)
    transactionType = Column(String(45))
    transactionDetail = Column(String(1000))
    ejId = Column(Integer, ForeignKey(ElectronicJournal.ejId))


# Create all tables in the database (comment out if tables already exist)
Base.metadata.create_all(engine)

# Open a session
session = sessionmaker(bind=engine)()

# Load JSON data
import json
with open("dummy.json", "r") as f:
    data = json.load(f)

# Iterate through each table in the JSON data
for table_name, table_data in data.items():
    # Get the corresponding table model class
    table_model = getattr(sys.modules[__name__], table_name)

    # Insert data into the table
    for row in table_data:
        session.add(table_model(**row))

# Commit changes to the database
session.commit()

# Close the session
session.close()

print("Data successfully populated from JSON file.")
