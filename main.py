from fastapi import FastAPI
from datetime import datetime, timezone, timedelta
from pydantic import BaseModel

app = FastAPI()


class Horarios(BaseModel):
    horario_3: str
    horario_5: str


@app.get("/", response_model=Horarios)
async def get_horarios():
    tz_3 = timezone(timedelta(hours=-3))
    tz_5 = timezone(timedelta(hours=-5))

    horario_3 = datetime.now(tz_3)
    horario_5 = datetime.now(tz_5)

    horario_3_str = horario_3.strftime("%Y-%m-%d %H:%M:%S")
    horario_5_str = horario_5.strftime("%Y-%m-%d %H:%M:%S")

    return {"horario_3": horario_3_str, "horario_5": horario_5_str}
