from sqlalchemy.orm import Session,joinedload
from models import *
from schemas import *


def get_employees(db: Session, skip: int = 0, limit: int = 100):
    #return db.query(Employee).offset(skip).limit(limit).all()
    return db.query(Employee).options(joinedload(Employee.asset)).all()


def get_employee_by_id(db: Session, emp_id: int):
    return db.query(Employee).filter(Employee.EmpId == emp_id).first()


def create_employee(db: Session, emp: EmployeeSchema):
    _emp = Employee(EmpId=emp.EmpId, FirstName=emp.FirstName, LastName=emp.LastName, Gender=emp.Gender, PhoneNumber=emp.PhoneNumber,Email=emp.Email, Address=emp.Address, BloodGroup=emp.BloodGroup, EmergencyContactNumber=emp.EmergencyContactNumber)
    db.add(_emp)
    db.commit()
    db.refresh(_emp)
    return _emp


def remove_employee(db: Session, emp_id: int):
    _emp = get_employee_by_id(db,emp_id)
    db.delete(_emp)
    db.commit()


def update_employee(db: Session, EmpId: int, FirstName: str, LastName: str, Gender: str, PhoneNumber: str, Email: str, Address: str, BloodGroup: str, EmergencyContactNumber: str):
    _emp = get_employee_by_id(db=db, emp_id=EmpId)

    _emp.EmpId=EmpId
    _emp.FirstName= FirstName
    _emp.LastName=LastName
    _emp.Gender=Gender
    _emp.PhoneNumber=PhoneNumber
    _emp.Email=Email
    _emp.Address=Address
    _emp.BloodGroup=BloodGroup
    _emp.EmergencyContactNumber=EmergencyContactNumber

    db.commit()
    db.refresh(_emp)
    return _emp


def get_assets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Asset).offset(skip).limit(limit).all()

def get_asset_by_id(db: Session, asset_id: int):
    return db.query(Asset).filter(Asset.Id == asset_id).first()

def create_asset(db: Session, asset: AssetSchema):
    _asset = Asset(Id=asset.Id, Name=asset.Name, Type=asset.Type)
    db.add(_asset)
    db.commit()
    db.refresh(_asset)
    return _asset

def remove_asset(db: Session, asset_id: int):
    _asset = get_asset_by_id(db,asset_id)
    db.delete(_asset)
    db.commit()

def update_asset(db: Session, Id: int, Name: str, Type: str):
    _asset = get_asset_by_id(db=db, asset_id=Id)

    _asset.Id=Id
    _asset.Name= Name
    _asset.Type=Type

    db.commit()
    db.refresh(_asset)
    return _asset

def add_employee_asset(db: Session, ES: EmpAssetSchema):
    _emp_asset = EmpAsset(emp_id=ES.empId, asset_id=ES.assetId)
    db.add(_emp_asset)
    db.commit()
    db.refresh(_emp_asset)
    return _emp_asset