from pydantic import BaseModel

class ConversionRates(BaseModel):
    USD : float
    XOF : float
    EUR : float
    CNY : float

class BaseSchemas(BaseModel):
    result : str
    conversion_rates : ConversionRates
