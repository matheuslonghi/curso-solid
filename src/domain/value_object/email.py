from pydantic import BaseModel, EmailStr


class Email(BaseModel):
    adress: str

    def domain(self) -> str:
        return self.adress.split("@")[1]