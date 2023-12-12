from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import uvicorn
from app.db.base import SessionLocal, engine
from app.router.router import router
#from app.models.Base.metadata.create_all(bind=engine)
from app.db.base import get_db
from app.model.base import Base
Base.metadata.create_all(bind=engine, checkfirst=True) 

app = FastAPI(title="Phát triển phần mềm hướng dịch vụ",
        docs_url='/docs',
        # docs_url=None,
        redoc_url=None,
        openapi_url=f"/openapi.json",
        description='''ONCENTER PROJECTS''',)



@app.get("/openapi.json", include_in_schema=False)
async def get_openapi_json():
    return app.openapi()




app.include_router(router, prefix="/app")

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=5000, debug=False, reload=False, workers=4)




