from fastapi import APIRouter, HTTPException
from app.models.schemas import SignalModel
from app.services.supabase_service import db_service

router = APIRouter(prefix="/iblm", tags=["IBLM"])

@router.post("/signal")
async def record_signal(signal: SignalModel):
    """
    Endpoint to receive real-time behavioral signals.
    """
    try:
        # Save to Supabase
        await db_service.log_signal(signal.dict())
        return {"status": "success", "message": "Signal recorded"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/kernel/{user_id}")
async def get_user_kernel(user_id: str):
    """
    Fetch the persistent 'Brain' state for a specific user.
    """
    kernel = await db_service.get_kernel(user_id)
    if not kernel:
        raise HTTPException(status_code=404, detail="Kernel not found")
    return kernel
