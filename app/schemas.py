from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class EmployeeSchema(BaseModel):
    EmpId: Optional[int] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    Gender: Optional[str] = None      
    PhoneNumber: Optional[str] = None
    Email: Optional[str] = None       
    Address: Optional[str] = None     
    BloodGroup: Optional[str] = None  
    EmergencyContactNumber: Optional[str] = None
    AssetCount: Optional[int] = None

    class Config:
        orm_mode = True

class RequestEmployee(BaseModel):
    parameter: EmployeeSchema = Field(...)



class AssetSchema(BaseModel):
    Id: Optional[int] = None
    Name: Optional[str] = None
    Type: Optional[str] = None

    class Config:
        orm_mode = True

class RequestAsset(BaseModel):
    parameter: AssetSchema = Field(...)



    


class EmpAssetSchema(BaseModel):
    empId: Optional[int] = None
    assetId: Optional[int] = None
   

    class Config:
        orm_mode = True

class RequestEmpAsset(BaseModel):
    parameter: EmpAssetSchema = Field(...)



class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]