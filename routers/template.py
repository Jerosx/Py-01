"""Plantilla para inicialización de endpoints."""

from fastapi import APIRouter

router = APIRouter(
    prefix='/template',
    tags=["Template"]
)

@router.get('/')
def endpoint_template()->None:
    """Endpoint plantilla que funciona como ejemplo de creación de nuevos endpoints"""
    return {"message": "Hola!, está es una muestra de inicialización de endpoints :D"}
