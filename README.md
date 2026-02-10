# Dark-Deployment

ssh -L 4242:localhost:4242 sandeshs@34.93.3.80
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
