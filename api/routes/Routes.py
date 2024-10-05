import os
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def home():
	return "Rogers Hackathon API home"
