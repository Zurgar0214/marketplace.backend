from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer

from dddpy.application.Services.authService import get_user_by_username_and_role
from dddpy.insfrastructure.Auth.jwt_manage import decode_jwt


class JWTBearer(HTTPBearer):

    async def __call__(self, request: Request):
        credentials = await super().__call__(request)
        
        data = decode_jwt(credentials.credentials)
        
        if data:
            #TODO: Cambiar esto a un servicio.
            user = get_user_by_username_and_role(data)
            
            if user:
                return user
            else:
                raise HTTPException(status_code=403, detail="Invalid authorization code")
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code")