# 🍕 Pizza Ordering Backend (Python)

A modular, object-oriented backend system for managing pizza orders with customizable sizes, crusts, toppings, and additional items like drinks and desserts. Designed with SOLID principles, discount policies, and extensible persistence.

> Originally inspired by a real-world Amazon SDE interview question, this project showcases production-quality code and OOP design patterns for service-oriented backend logic.

---

## ✅ Features

- Object-oriented models for `Pizza`, `Drink`, `Dessert`
- Custom pricing per pizza size, crust, and toppings
- Order system supporting multiple items
- Discount policy support (e.g. 50% off highest priced pizza with an order of 2 or more)
- Swappable persistence layer (currently in-memory)
- Unit-tested with `pytest`
- CI setup with GitHub Actions
- Dockerized for easy deployment

---

## 🗂️ Project Structure

```bash
pizza_ordering_backend/
├── app/
│   ├── models/          # Pizza, Drink, Dessert classes
│   ├── entities/        # Order object
│   ├── services/        # Discounts, order processing
│   ├── persistence/     # In-memory repo, can be swapped
│   └── config/          # Pricing config
├── scripts/             # Entry point scripts
├── tests/               # Pytest unit tests
├── Dockerfile           # App container
├── docker-compose.yml   # Service runner
├── .github/workflows/   # CI pipeline
└── README.md            # You're here!
```

---

## 🚀 Getting Started

### 🐳 Run with Docker

```bash
docker compose up --build
```

### 🔬 Run Locally (Python 3.13+)

```bash
pip install -r requirements.txt
PYTHONPATH=. pytest
PYTHONPATH=. python scripts/run_example.py
```

---

## 🧪 Testing

```bash
PYTHONPATH=. pytest tests/
```

Tests cover model pricing, descriptions, discounts, and persistence behavior.

---

## 🏗️ Example Output

```text
Order summary:
- Small pizza with thin crust and toppings: 
- Medium pizza with thick crust and toppings: pepperoni
- Large pizza with stuffed crust and toppings: pepperoni, mushrooms, onions
- Brownie
- Ice cream
- Medium Coke
- Large Coke
Total with discount: $38.88
```

---

## 🔐 License

This project is licensed under the MIT License. See [`LICENSE`](./LICENSE) for details.

---

## ✨ Want to Expand It?

- Add RESTful API with FastAPI or Flask
- Plug in SQLite or PostgreSQL via SQLAlchemy
- Add user sessions, authentication
- Web front-end with React or Vue
- Offer scheduled delivery / loyalty discounts
