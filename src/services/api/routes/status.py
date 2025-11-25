from fastapi import APIRouter

router = APIRouter(prefix="/status", tags=["Status"])


@router.get("/")
async def get_status():
    return {"status": "API is running smoothly, just like it should."}
