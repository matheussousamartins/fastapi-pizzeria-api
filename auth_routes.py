from fastapi import APIRouter, Depends, HTTPException
from models import Users
from dependencies import get_session
from main import bcrypt_context
from schemas import UserSchema
from sqlalchemy.orm import Session


auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    """
    Essa é a rota padrão de autenticação do sistema.
    """
    return {
        "mensagem": "Você acessou a rota padrão de autenticação", 
        "autenticado": False
    }

@auth_router.post("/create_account")
async def create_account(user_schema: UserSchema, session: Session = Depends(get_session)):
    user = session.query(Users).filter(Users.email == user_schema.email).first()
    if user:
        raise HTTPException(status_code=400,detail="E-mail do usuário já cadastrado")
    else:
        encrypted_password = bcrypt_context.hash(user_schema.password)
        new_user = Users(user_schema.name, user_schema.phone, user_schema.email, encrypted_password, user_schema.active, user_schema.admin)  
        session.add(new_user)
        session.commit()
        return {"mensagem": f"usuário cadastrado com sucesso: {user_schema.email}"}

