from aiogram import Router

from .price import price_router
from .start import start_router

main_router = Router()
main_router.include_router(start_router)
main_router.include_router(price_router)
