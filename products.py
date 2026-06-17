import urllib.parse


def amazon_search_link(product_name: str) -> str:
    """Generate a real Amazon India search URL for a given product name."""
    query = urllib.parse.quote_plus(product_name)
    return f"https://www.amazon.in/s?k={query}"


PRODUCTS = [
    # ── LAPTOPS ──────────────────────────────────────────────────────────
    {
        "id": 1,
        "name": "Lenovo IdeaPad Slim 3",
        "category": "Laptop",
        "price": 32999,
        "original_price": 45000,
        "discount": 27,
        "rating": 4.2,
        "tags": ["coding", "college", "budget", "student"],
        "specs": {"RAM": "8GB", "Storage": "512GB SSD", "Processor": "Intel i5", "Display": "15.6 inch"},
        "description": "Lightweight laptop perfect for everyday college use and coding.",
        "buy_link": amazon_search_link("Lenovo IdeaPad Slim 3")
    },
    {
        "id": 2,
        "name": "ASUS VivoBook 15",
        "category": "Laptop",
        "price": 38999,
        "original_price": 52000,
        "discount": 25,
        "rating": 4.3,
        "tags": ["design", "college", "student", "multimedia"],
        "specs": {"RAM": "16GB", "Storage": "512GB SSD", "Processor": "AMD Ryzen 5", "Display": "15.6 inch FHD"},
        "description": "Great for design students with vibrant display and good performance.",
        "buy_link": amazon_search_link("ASUS VivoBook 15")
    },
    {
        "id": 3,
        "name": "HP Pavilion 15",
        "category": "Laptop",
        "price": 55999,
        "original_price": 70000,
        "discount": 20,
        "rating": 4.4,
        "tags": ["coding", "gaming", "student", "premium"],
        "specs": {"RAM": "16GB", "Storage": "1TB SSD", "Processor": "Intel i7", "Display": "15.6 inch IPS"},
        "description": "Premium performance laptop for heavy coding and multitasking.",
        "buy_link": amazon_search_link("HP Pavilion 15")
    },
    {
        "id": 4,
        "name": "Acer Aspire Lite",
        "category": "Laptop",
        "price": 27999,
        "original_price": 35000,
        "discount": 20,
        "rating": 4.0,
        "tags": ["budget", "student", "college", "basic"],
        "specs": {"RAM": "8GB", "Storage": "256GB SSD", "Processor": "Intel i3", "Display": "15.6 inch"},
        "description": "Ultra-affordable laptop for students on a tight budget.",
        "buy_link": amazon_search_link("Acer Aspire Lite")
    },

    # ── PHONES ───────────────────────────────────────────────────────────
    {
        "id": 5,
        "name": "Redmi Note 13 Pro",
        "category": "Phone",
        "price": 23999,
        "original_price": 29999,
        "discount": 20,
        "rating": 4.5,
        "tags": ["camera", "student", "budget", "social media"],
        "specs": {"RAM": "8GB", "Storage": "256GB", "Camera": "200MP", "Battery": "5100mAh"},
        "description": "Best camera phone under 25K for photography enthusiasts.",
        "buy_link": amazon_search_link("Redmi Note 13 Pro")
    },
    {
        "id": 6,
        "name": "Samsung Galaxy M34",
        "category": "Phone",
        "price": 17999,
        "original_price": 24000,
        "discount": 25,
        "rating": 4.3,
        "tags": ["budget", "student", "battery life", "gaming"],
        "specs": {"RAM": "6GB", "Storage": "128GB", "Camera": "50MP", "Battery": "6000mAh"},
        "description": "Massive battery for long college days, budget-friendly.",
        "buy_link": amazon_search_link("Samsung Galaxy M34")
    },
    {
        "id": 7,
        "name": "OnePlus Nord CE 3",
        "category": "Phone",
        "price": 21999,
        "original_price": 27999,
        "discount": 21,
        "rating": 4.4,
        "tags": ["fast charging", "performance", "student"],
        "specs": {"RAM": "8GB", "Storage": "256GB", "Camera": "108MP", "Battery": "5000mAh"},
        "description": "Blazing fast performance and fast charging for busy students.",
        "buy_link": amazon_search_link("OnePlus Nord CE 3")
    },

    # ── HEADPHONES ───────────────────────────────────────────────────────
    {
        "id": 8,
        "name": "boAt Rockerz 450",
        "category": "Headphones",
        "price": 1299,
        "original_price": 3990,
        "discount": 67,
        "rating": 4.1,
        "tags": ["budget", "student", "music", "wireless"],
        "specs": {"Type": "Over-ear", "Battery": "15hrs", "Connectivity": "Bluetooth 5.0"},
        "description": "Best budget wireless headphones for students who love music.",
        "buy_link": amazon_search_link("boAt Rockerz 450")
    },
    {
        "id": 9,
        "name": "Sony WH-1000XM4",
        "category": "Headphones",
        "price": 19990,
        "original_price": 29990,
        "discount": 33,
        "rating": 4.7,
        "tags": ["premium", "noise cancelling", "study", "focus"],
        "specs": {"Type": "Over-ear", "Battery": "30hrs", "Connectivity": "Bluetooth 5.0", "ANC": "Yes"},
        "description": "Industry-leading noise cancellation for focused studying.",
        "buy_link": amazon_search_link("Sony WH-1000XM4")
    },

    # ── TABLETS ──────────────────────────────────────────────────────────
    {
        "id": 10,
        "name": "Samsung Galaxy Tab A8",
        "category": "Tablet",
        "price": 16999,
        "original_price": 22999,
        "discount": 26,
        "rating": 4.2,
        "tags": ["student", "notes", "reading", "budget"],
        "specs": {"RAM": "4GB", "Storage": "64GB", "Display": "10.5 inch", "Battery": "7040mAh"},
        "description": "Great tablet for digital notes, reading PDFs, and online classes.",
        "buy_link": amazon_search_link("Samsung Galaxy Tab A8")
    },
    {
        "id": 11,
        "name": "Xiaomi Pad 6",
        "category": "Tablet",
        "price": 22999,
        "original_price": 30000,
        "discount": 23,
        "rating": 4.5,
        "tags": ["premium", "student", "productivity", "notes"],
        "specs": {"RAM": "6GB", "Storage": "128GB", "Display": "11 inch 144Hz", "Battery": "8840mAh"},
        "description": "High refresh rate display ideal for design and media students.",
        "buy_link": amazon_search_link("Xiaomi Pad 6")
    },

    # ── BAGS ─────────────────────────────────────────────────────────────
    {
        "id": 12,
        "name": "Skybags Campus 30L Backpack",
        "category": "Bag",
        "price": 999,
        "original_price": 1999,
        "discount": 50,
        "rating": 4.3,
        "tags": ["budget", "college", "student", "backpack"],
        "specs": {"Capacity": "30L", "Laptop Compartment": "15 inch", "Material": "Polyester"},
        "description": "Spacious and stylish college backpack at an unbeatable price.",
        "buy_link": amazon_search_link("Skybags Campus 30L Backpack")
    },
    {
        "id": 13,
        "name": "American Tourister Laptop Bag",
        "category": "Bag",
        "price": 1799,
        "original_price": 3500,
        "discount": 49,
        "rating": 4.4,
        "tags": ["premium", "college", "student", "laptop bag"],
        "specs": {"Capacity": "25L", "Laptop Compartment": "15.6 inch", "Material": "Nylon"},
        "description": "Durable premium laptop bag for engineering and IT students.",
        "buy_link": amazon_search_link("American Tourister Laptop Bag")
    },

    # ── STATIONERY ───────────────────────────────────────────────────────
    {
        "id": 14,
        "name": "Faber-Castell Grip Pen Set",
        "category": "Stationery",
        "price": 299,
        "original_price": 499,
        "discount": 40,
        "rating": 4.6,
        "tags": ["student", "writing", "budget", "stationery"],
        "specs": {"Count": "10 pens", "Type": "Ballpoint", "Grip": "Ergonomic"},
        "description": "Comfortable grip pens for long writing sessions and exams.",
        "buy_link": amazon_search_link("Faber-Castell Grip Pen Set")
    },
    {
        "id": 15,
        "name": "Classmate A4 Spiral Notebooks (5 pack)",
        "category": "Stationery",
        "price": 349,
        "original_price": 550,
        "discount": 37,
        "rating": 4.4,
        "tags": ["student", "notes", "budget", "stationery", "college"],
        "specs": {"Pages": "200 pages each", "Type": "Spiral", "Size": "A4"},
        "description": "Pack of 5 spiral notebooks for all your college subjects.",
        "buy_link": amazon_search_link("Classmate A4 Spiral Notebooks")
    },
]