from sqlalchemy import  Column, ForeignKey, Integer, String, Table
from config import Base
from sqlalchemy.orm import relationship

employee_asset = Table("employee_asset", Base.metadata,
                       Column("empId", ForeignKey("employee.EmpId"), primary_key=True),
                       Column("assetId", ForeignKey("asset.Id"), primary_key=True))


class Employee(Base):
    __tablename__ ="employee"

    EmpId = Column(Integer, primary_key=True, index=True)
    FirstName = Column(String)
    LastName = Column(String)
    Gender= Column(String)
    PhoneNumber=Column(String)
    Email= Column(String)
    Address= Column(String)
    BloodGroup= Column(String)
    EmergencyContactNumber= Column(String)
    AssetCount = Column(Integer)

    asset = relationship("Asset",
                           secondary=employee_asset,
                           back_populates="employee")

class Asset(Base):
    __tablename__ ="asset"

    Id = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    Type = Column(String)

    employee = relationship("Employee",
                           secondary=employee_asset,
                           back_populates="asset")
    