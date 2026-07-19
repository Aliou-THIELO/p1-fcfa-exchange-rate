from pydantic import BaseModel, model_validator

class ConversionRates(BaseModel):
    USD : float
    XOF : float
    EUR : float
    CNY : float

    @model_validator(mode="after")
    def check_positive_rates(self):
        for nom, valeur in [("USD", self.USD), ("XOF", self.XOF), ("EUR", self.EUR), ("CNY", self.CNY)]:
         if valeur <= 0:
            raise ValueError(f"{nom} rate must be positive, got {valeur}")
         return self

class BaseSchemas(BaseModel):
    result : str
    conversion_rates : ConversionRates
