from fastapi import APIRouter, Depends, HTTPException
from models import Users
from dependencies import get_session
from main import bcrypt_context
from schemas import UserSchema, LoginSchema
from sqlalchemy.orm import Session


auth_router = APIRouter(prefix="/auth", tags=["auth"])

def create_token(user_id):
    token = f"fjhioweuhrwpj{user_id}" # temporário/manual
    return token

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


@auth_router.post("/login")
async def login(login_schema: LoginSchema, session: Session = Depends(get_session)):
    user = session.query(Users).filter(Users.email == login_schema.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Usuário não encontrado")
    else:
        access_token = create_token(user.id)
        return {
            "access_token": access_token,
            "token_type": "Bearer"
        }
        
    







