"""Modulo de carga de routers automaticos."""

from fastapi import FastAPI

from pathlib import Path
import importlib


def register_routers(app: FastAPI) -> None:
    """Registra automáticamente todos los routers definidos en la carpeta
    'routers'.

    La función recorre todos los archivos Python ('*.py') dentro de la
    carpeta 'routers', excluyendo aquellos cuyo nombre comienza con "_".
    Cada módulo es importado dinámicamente y, si contiene una variable
    llamada 'router' de tipo APIRouter, esta se registra en la aplicación
    FastAPI mediante 'include_router()'.

    Args:
        app (FastAPI): Instancia principal de la aplicación FastAPI donde
            se registrarán los routers encontrados.

    Example:
        Estructura esperada:

        project/
        ├── main.py
        ├── routers/
        │   ├── auth.py
        │   └── users.py
        └── utils/
            └── router_loader.py

        Contenido de auth.py:

        router = APIRouter(
            prefix="/auth",
            tags=["Auth"]
        )

        Al ejecutar:

        register_routers(app)

        El router será registrado automáticamente y sus endpoints quedarán
        disponibles en la aplicación.

    Notes:
        - Los módulos deben exponer una variable llamada 'router'.
        - Los archivos cuyo nombre comience por "_" serán ignorados.
        - La ruta de importación utilizada es 'routers.<nombre_modulo>'.

    """

    routers_path = Path(__file__).parent.parent / 'routers'

    for file in routers_path.glob('*.py'):
        if file.stem.startswith('_'):
            continue

        module = importlib.import_module(
            f'routers.{file.stem}'
        )

        router = getattr(module, 'router', None)

        if router:
            app.include_router(router)
