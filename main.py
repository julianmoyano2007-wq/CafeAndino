from pathlib import Path
from uuid import uuid4

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="Cafe Andino",
    docs_url=None,
    redoc_url=None
)

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

MENU = [
    {
        "id": "espresso-andino",
        "nombre": "Espresso Andino",
        "categoria": "Cafes calientes",
        "precio": 4500,
        "descripcion": "Shot corto, intenso y aromatico.",
        "etiqueta": "Origen",
        "icono": "☕"
    },
    {
        "id": "americano-cumbre",
        "nombre": "Americano Cumbre",
        "categoria": "Cafes calientes",
        "precio": 5900,
        "descripcion": "Cafe largo, balanceado y de cuerpo limpio.",
        "etiqueta": "Clasico",
        "icono": "☕"
    },
    {
        "id": "latte-altura",
        "nombre": "Latte de Altura",
        "categoria": "Cafes calientes",
        "precio": 8900,
        "descripcion": "Espresso con leche cremosa y textura suave.",
        "etiqueta": "Cremoso",
        "icono": "🥛"
    },
    {
        "id": "capuccino-valle",
        "nombre": "Capuccino del Valle",
        "categoria": "Cafes calientes",
        "precio": 8900,
        "descripcion": "Espresso, leche vaporizada y espuma sedosa.",
        "etiqueta": "Favorito",
        "icono": "☁️"
    },
    {
        "id": "moka-sierra",
        "nombre": "Moka Sierra",
        "categoria": "Cafes calientes",
        "precio": 9600,
        "descripcion": "Cafe, chocolate y leche en una mezcla envolvente.",
        "etiqueta": "Chocolate",
        "icono": "🍫"
    },
    {
        "id": "macchiato-nevado",
        "nombre": "Macchiato Nevado",
        "categoria": "Cafes calientes",
        "precio": 7900,
        "descripcion": "Espresso con un toque ligero de leche.",
        "etiqueta": "Intenso",
        "icono": "❄️"
    },
    {
        "id": "chocolate-origen",
        "nombre": "Chocolate de Origen",
        "categoria": "Cafes calientes",
        "precio": 8500,
        "descripcion": "Bebida caliente cremosa con sabor profundo.",
        "etiqueta": "Tradicion",
        "icono": "🍫"
    },
    {
        "id": "latte-helado-andino",
        "nombre": "Latte Helado Andino",
        "categoria": "Bebidas frias",
        "precio": 9900,
        "descripcion": "Espresso frio con leche y hielo.",
        "etiqueta": "Refrescante",
        "icono": "🧊"
    },
    {
        "id": "cold-brew-paramo",
        "nombre": "Cold Brew Paramo",
        "categoria": "Bebidas frias",
        "precio": 9500,
        "descripcion": "Extraccion en frio de sabor limpio y elegante.",
        "etiqueta": "Frio",
        "icono": "🧋"
    },
    {
        "id": "moka-frio-dorado",
        "nombre": "Moka Frio Dorado",
        "categoria": "Bebidas frias",
        "precio": 10200,
        "descripcion": "Cafe frio con notas de chocolate y leche.",
        "etiqueta": "Top",
        "icono": "🧊"
    },
    {
        "id": "frappe-caramelo-andino",
        "nombre": "Frappe Caramelo Andino",
        "categoria": "Bebidas frias",
        "precio": 12500,
        "descripcion": "Bebida frappe cremosa con perfil dulce.",
        "etiqueta": "Frappe",
        "icono": "🥤"
    },
    {
        "id": "frappe-cookies-montana",
        "nombre": "Frappe Cookies Montana",
        "categoria": "Bebidas frias",
        "precio": 12900,
        "descripcion": "Bebida helada inspirada en galleta y cafe.",
        "etiqueta": "Postre",
        "icono": "🍪"
    },
    {
        "id": "limonada-cafe-campo",
        "nombre": "Limonada de Cafe Campo",
        "categoria": "Bebidas frias",
        "precio": 9200,
        "descripcion": "Toque citrico con cafe frio, ligera y diferente.",
        "etiqueta": "Nuevo",
        "icono": "🍋"
    },
    {
        "id": "croissant-queso-paramo",
        "nombre": "Croissant Queso del Paramo",
        "categoria": "Panaderia y snacks",
        "precio": 7200,
        "descripcion": "Hojaldre dorado con relleno suave de queso.",
        "etiqueta": "Horneado",
        "icono": "🥐"
    },
    {
        "id": "pan-chocolate-sierra",
        "nombre": "Pan de Chocolate Sierra",
        "categoria": "Panaderia y snacks",
        "precio": 6900,
        "descripcion": "Pieza de panaderia con centro de chocolate.",
        "etiqueta": "Dulce",
        "icono": "🍫"
    },
    {
        "id": "muffin-arandanos-bosque",
        "nombre": "Muffin Arandanos Bosque",
        "categoria": "Panaderia y snacks",
        "precio": 6800,
        "descripcion": "Muffin suave con sabor frutal.",
        "etiqueta": "Bakery",
        "icono": "🫐"
    },
    {
        "id": "galleta-doble-cacao",
        "nombre": "Galleta Doble Cacao",
        "categoria": "Panaderia y snacks",
        "precio": 5200,
        "descripcion": "Galleta grande con sabor intenso a cacao.",
        "etiqueta": "Snack",
        "icono": "🍪"
    },
    {
        "id": "sandwich-campesino",
        "nombre": "Sandwich Campesino",
        "categoria": "Panaderia y snacks",
        "precio": 14900,
        "descripcion": "Sandwich salado para una comida ligera.",
        "etiqueta": "Salado",
        "icono": "🥪"
    },
    {
        "id": "torta-zanahoria-hogar",
        "nombre": "Torta de Zanahoria Hogar",
        "categoria": "Panaderia y snacks",
        "precio": 9500,
        "descripcion": "Porcion suave con cobertura dulce.",
        "etiqueta": "Postre",
        "icono": "🍰"
    }
]

class ItemOrden(BaseModel):
    product_id: str
    cantidad: int = Field(ge=1, le=20)

class OrdenIn(BaseModel):
    cliente: str = Field(min_length=2, max_length=60)
    items: list[ItemOrden]

@app.get("/")
def home():
    return FileResponse(BASE_DIR / "index.html")

@app.get("/api/menu")
def obtener_menu():
    return {
        "marca": "Cafe Andino",
        "menu": MENU
    }

@app.post("/api/orden")
def crear_orden(orden: OrdenIn):
    cliente = orden.cliente.strip()

    if not cliente:
        raise HTTPException(status_code=400, detail="Debes ingresar tu nombre.")

    if not orden.items:
        raise HTTPException(status_code=400, detail="No hay productos en el pedido.")

    catalogo = {producto["id"]: producto for producto in MENU}

    detalle = []
    total = 0

    for item in orden.items:
        producto = catalogo.get(item.product_id)

        if producto is None:
            raise HTTPException(
                status_code=404,
                detail=f"Producto no encontrado: {item.product_id}"
            )

        subtotal = producto["precio"] * item.cantidad
        total += subtotal

        detalle.append({
            "id": producto["id"],
            "nombre": producto["nombre"],
            "cantidad": item.cantidad,
            "precio_unitario": producto["precio"],
            "subtotal": subtotal
        })

    return {
        "ok": True,
        "codigo": uuid4().hex[:8].upper(),
        "cliente": cliente,
        "total": total,
        "items": detalle,
        "mensaje": "Pedido registrado con exito"
    }
