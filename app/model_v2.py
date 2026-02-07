def predict(data):
    score = data["income"] * 0.6 + data["credit_score"] * 0.4
    return "APPROVED" if score > 60000 else "REJECTED"

