from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import *

import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/createEmployee")
async def create_employee_service(request: RequestEmployee, db: Session = Depends(get_db)):
    crud.create_employee(db, request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Employee created successfully").dict(exclude_none=True)


@router.get("/employee")
async def get_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _emp = crud.get_employees(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_emp)

@router.get("/employee/{emp_id}")
def emp_by_id(emp_id: int, db: Session = Depends(get_db)):
    _emp = crud.get_employee_by_id(db,emp_id)
    return Response(status="Ok", code="200", message="Success fetch data", result=_emp)

@router.patch("/updateEmployee")
async def update_employee(request: RequestEmployee, db: Session = Depends(get_db)):
    _emp = crud.update_employee(db, EmpId=request.parameter.EmpId,
                             FirstName=request.parameter.FirstName,
                             LastName=request.parameter.LastName,
                             Gender=request.parameter.Gender,
                             PhoneNumber=request.parameter.PhoneNumber,
                             Email=request.parameter.Email,
                             Address=request.parameter.Address,
                             BloodGroup=request.parameter.BloodGroup,
                             EmergencyContactNumber=request.parameter.EmergencyContactNumber
                             )
    return Response(status="Ok", code="200", message="Success update data", result=_emp)

@router.delete("/deleteEmployee/{emp_id}")
async def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    crud.remove_employee(db,emp_id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)

###########################################################################################################3

@router.get("/assets")
async def get_assets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _asset = crud.get_assets(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_asset)

@router.get("/assets/{asset_id}")
def asset_by_id(asset_id: int, db: Session = Depends(get_db)):
    _emp = crud.get_asset_by_id(db,asset_id)
    return Response(status="Ok", code="200", message="Success fetch data", result=_emp)

@router.post("/createAsset")
async def create_asset_service(request: RequestAsset, db: Session = Depends(get_db)):
    crud.create_asset(db, request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Asset created successfully").dict(exclude_none=True)


@router.delete("/deleteAsset/{asset_id}")
async def delete_asset(asset_id: int, db: Session = Depends(get_db)):
    crud.remove_asset(db,asset_id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)

@router.patch("/updateAsset")
async def update_asset(request: RequestAsset, db: Session = Depends(get_db)):
    _asset = crud.update_asset(db, Id=request.parameter.Id,
                             Name=request.parameter.Name,
                             Type=request.parameter.Type,
                             )
    return Response(status="Ok", code="200", message="Success update data", result=_asset)

@router.post("/addEmpAsset")
async def add_emp_asset(request: RequestEmpAsset, db: Session = Depends(get_db)):
    crud.add_employee_asset(db, request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Employee asset created successfully").dict(exclude_none=True)