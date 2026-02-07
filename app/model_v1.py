def predict(data):
    if data["income"] > 50000:
        return "APPROVED"
    return "REJECTED"

