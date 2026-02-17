from fastapi import APIRouter

order_router = APIRouter(prefix="/orders", tags=["orders"])

@order_router.get("/")
async def orders():
    """
    Essa é a rota padrão de pedidos do sistema.
    Todas as rotas dos pedidos precisam de autenticação.
    """
    return {"mensagem": "Você acessou a rota de orders"}