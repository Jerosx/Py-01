"""Punto de entrada de la aplicación.

Este módulo inicia el servidor ASGI utilizando Uvicorn y expone la
aplicación FastAPI definida en 'main.py'.

Configuración por defecto:
    - Host: 0.0.0.0
    - Puerto: 8000
    - Recarga automática habilitada (reload=True)

Uso:
    python run.py

"""

import uvicorn

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
        reload=True
    )
