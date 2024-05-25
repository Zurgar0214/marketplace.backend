
def validate_password(db_user: UserDTO, user:UserLogin):
    if db_user.password == user.password:
            
        token = get_token(UserModel(**db_user.__dict__).__dict__)

        return token
    else:
        return None
    
def get_token(data: dict):
    return encode_jwt(data)