from fastapi import FastAPI
#from model_v1 import predict as v1_predict
#from model_v2 import predict as v2_predict
from model_v1 import predict as v1_predict
from model_v2 import predict as v2_predict
from feature_flag import is_enabled, init_unleash, shutdown_unleash
from metrics import REQUEST_COUNT, PREDICTION_LATENCY
import time

app = FastAPI()
@app.on_event("startup")
def _startup():
    init_unleash()

@app.on_event("shutdown")
def _shutdown():
    shutdown_unleash()

@app.post("/predict")
def predict(data: dict):
    start = time.time()
    v1_result = v1_predict(data)

    # Shadow execution
    v2_result = v2_predict(data)

    print({
        "input": data,
        "v1": v1_result,
        "v2": v2_result
    })

    if is_enabled("model_v2_enabled"):
        REQUEST_COUNT.labels("v2").inc()
        PREDICTION_LATENCY.labels("v2").observe(time.time() - start)
        return {"decision": v2_result, "model": "v2"}

    REQUEST_COUNT.labels("v1").inc()
    PREDICTION_LATENCY.labels("v1").observe(time.time() - start)
    return {"decision": v1_result, "model": "v1"}
