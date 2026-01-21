from aiogram import Router

from .main import main_router

router = Router()

router.include_router(main_router)
