from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/ai", tags=["AI"])


@router.get("/settlement-predictor")
def settlement():

    try:

        return {
            "prediction": "65%",
            "status": "Success"
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
