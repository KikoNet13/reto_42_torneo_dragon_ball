import reflex as rx

config = rx.Config(
    app_name="app",
    frontend_port=8081,
    backend_port=8001,
    api_url="https://reto42-api-kikonet13.duckdns.org",
    cors_allowed_origins=[
        "http://localhost:8081",
        "http://127.0.0.1:8081",
        "http://192.168.1.2:8081",
        "https://reto42-kikonet13.duckdns.org",
        "https://kikonet13.reflex.run",
    ],
)
