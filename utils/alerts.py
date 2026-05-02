def risk_alerts(temp, humidity, rainfall, ph):
    alerts = []

    if rainfall < 40:
        alerts.append("Low rainfall risk. Irrigation recommended.")

    if humidity > 85:
        alerts.append("High humidity may increase fungal disease risk.")

    if temp > 38:
        alerts.append("Heat stress risk.")

    if ph < 5.5 or ph > 8:
        alerts.append("Soil pH outside optimal range.")

    return alerts