from pydantic import BaseModel, field_validator
from typing import Literal

class Ticket(BaseModel):
    title : str
    description : str
    priority : Literal["Low", "Medium", "High"] = "Medium"
    status : Literal["Open", "In Progress", "On Hold", "Resolved", "Closed"] = "Open"

    @field_validator("title")
    def validate_title(cls, value):
        value = value.strip()
        if value == "":
            raise ValueError("Title contains only spaces")

        return value

    @field_validator("description")
    def validate_description(cls, value):
        value = value.strip()
        if value == "":
            raise ValueError("Description contains only spaces")

        return value


t1 = Ticket(
    title = "Laptop not working",
    description = "Laptop is not turning on",
    status = "Open"
)

print(t1)

t2 = Ticket(
    title = " ",
    description = "issue with my laptop",
    priority = "High"
)

print(t2)

#t3 = Ticket(description = "Issue with my laptop")
#print(t3) >> ValidationError: 1 validation error for Ticket title

'''t4 = Ticket(
    title = "issue",
    description = "issue with my laptop",
    priority = "Super Critical"
)'''
#Input should be 'Low', 'Medium' or 'High' 