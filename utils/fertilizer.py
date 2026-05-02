def recommend_fertilizer(N, P, K, ph):
    advice = []

    if N < 50:
        advice.append("Low Nitrogen: Apply Urea.")
    if P < 40:
        advice.append("Low Phosphorus: Apply DAP.")
    if K < 40:
        advice.append("Low Potassium: Apply MOP.")
    if ph < 5.5:
        advice.append("Soil acidic: Apply lime.")
    if ph > 8:
        advice.append("Soil alkaline: Use gypsum / organic matter.")

    return advice