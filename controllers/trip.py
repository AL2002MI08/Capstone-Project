from fastapi import APIRouter


router = APIRouter(tags=["Trip"])

@router.get("/", response_model=)
def get_trips(session: Session = Depends(deps.get_session)):
    return {"message": "Get trips"}