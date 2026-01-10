from fastapi import APIRouter, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .schemas import Product, ProductCreate

router = APIRouter(tags=['Products'], prefix="/products")


@router.get("/", response_model=list[Product])
async def get_products(session: AsyncSession):
    return await crud.get_products(session=session)

@router.post("/", response_model=Product)
async def create_product(session: AsyncSession, product_in: ProductCreate):
    return crud.create_product(session=session, product_in=product_in)

@router.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int, session: AsyncSession):
    product =  await crud.get_product(session=session, product_id=product_id)
    if product:
        return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {product_id} not found",
    )

