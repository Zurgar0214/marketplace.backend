from fastapi import FastAPI
from dddpy.insfrastructure.sqlite.database import Base, engine
from controllers.userController import user_router;
from controllers.authController import auth_router;


app = FastAPI(debug=True)
Base.metadata.create_all(bind= engine)
app.include_router(user_router)
app.include_router(auth_router)


@app.get(
        "/healthCheck",
        status_code=status.HTTP_200_OK
        )
async def healthCheck():
    '''app is already working!'''
    return {"message": "All works!"}



             

    
