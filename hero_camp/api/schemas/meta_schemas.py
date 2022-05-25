from pydantic import BaseModel, Field


class HTTPError(BaseModel):
    detail: str = Field(description="Error detail.", example="Somthing went wrong.")
