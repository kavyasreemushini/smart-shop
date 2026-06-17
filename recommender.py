def search_products(query, products):
    query_words = query.lower().split()
    scored = []
    for product in products:
        score = 0
        text = (product["name"] + " " + product["category"] + " " +
                product["description"] + " " + " ".join(product.get("tags", []))).lower()
        for word in query_words:
            if word in text:
                score += 1
            if word in product["name"].lower():
                score += 2
        if score > 0:
            scored.append((score, product))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [item[1] for item in scored]


def get_recommendations(budget, category, purpose, products):
    within_budget = [p for p in products if p["price"] <= budget]

    if category and category.lower() != "all":
        filtered = [p for p in within_budget if p["category"].lower() == category.lower()]
    else:
        filtered = within_budget

    purpose_words = purpose.lower().split() if purpose else []
    scored = []
    for product in filtered:
        score = product["rating"] * 10 + product["discount"]
        for word in purpose_words:
            if word in " ".join(product.get("tags", [])).lower():
                score += 15
        scored.append((score, product))

    scored.sort(key=lambda x: x[0], reverse=True)
    results = [item[1] for item in scored]

    tips = []
    if budget < 10000:
        tips.append("💡 Look for refurbished items for better specs.")
        tips.append("🎓 Use student discount codes on Flipkart and Amazon.")
    elif budget < 40000:
        tips.append("💡 Compare EMI options — many products have 0% EMI for students.")
    else:
        tips.append("💡 Buy during Big Billion Days for max savings.")

    best = results[0] if results else None
    savings = (best["original_price"] - best["price"]) if best else None

    return {
        "best_pick": best,
        "alternatives": results[1:4],
        "budget_tips": tips,
        "total_found": len(results),
        "savings_possible": savings
    }


def get_budget_deals(products, limit=6):
    return sorted(products, key=lambda p: p["discount"], reverse=True)[:limit]