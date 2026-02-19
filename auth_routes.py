from fastapi import APIRouter, Depends
from models import Users
from dependencies import get_session


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
async def create_account(name: str, phone: int, email: str, password: str, session = Depends(get_session)):
    user = session.query(Users).filter(Users.email == email).first()
    if user:
        return {"mensagem": "já existe um usuário com esse email"}
    else:
        new_user = Users(name, phone, email, password)  
        session.add(new_user)
        session.commit()
        return {"mensagem": "usuário cadastrado com sucesso"}

