#Today I am learning Pydantic, what's it? it is a library allows you to do data validation and serialization. It is very usefull, while defining an API, because you need to check whether the data is coming towards your API is validate and not hacked. So Pydantic is like a Dataclass with steriods, we see how we can check or validate the data using dataclass on previous day, using post_init() dunder method. Basemodel comes from Pydantic, it implements the bascis of validation system of Pydantic. 
#It is useful in IDE Type Hints / Data Validation / JSON Serialization
#It is better to use for data validation and JSON serialization when you have number of things to validate like many number of emails, also when data is complex. However same thing can be achieved with dataclass whose syntax similar to pydantic, but code will become little bit complex
from pydantic import (
    BaseModel,
    EmailStr, #By default this is have some validation, so it useful to use it directly rather than writing a whole
    Field, 
    SecretStr, #it is use to print something secret like password
    ValidationError,
    field_validator
)

class User_Profile(BaseModel):
    user_name:str = Field(examples=['Darshil','Rohan'])
    user_email:EmailStr = Field(examples=['darshil@gmail.com','darshil@yahoo.co.in'],frozen=True,description='It is the email of an user')
    user_password :SecretStr = Field(examples=['darshil@1234'],description='This is the password of an user')
    age:int= Field(description='Age must be between 18 to 100')
    
    @field_validator('age') #this is the way how we can validate or write a function to add extra logic to that perticular field
    @classmethod #it is imp to write this after field_validator, as it validator fun. get access to the class itself.(cls)
    def age_validator(cls,value):
        if not (18<=value<=100):
            raise ValidationError("age must be between 18 to 100")
        return value

def main():
    try:
        user1 = User_Profile(user_name='Darshil',user_email='darshil@gmail.com',user_password='Darshil@2025',age=23)
        print(f"This is the result of user 1 = {user1}")
        user2 = User_Profile(user_name='Kalp',user_email='kalpgmail.com',user_password='password',age=18)
        print(f"This is the result of user 2 = {user2}")
    except ValidationError as e:
        print(e)
        
if __name__ == "__main__":
    main()
