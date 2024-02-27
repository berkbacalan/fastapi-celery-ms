DATABASE_URL = "postgresql://admin:admin@postgres:5432/books"

CELERY_BROKER_URL = "redis://redis:6379/0"
CELERY_RESULT_BACKEND = "db+postgresql://admin:admin@postgres:5432/books"

# API KEY for auth
SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"


CORS_ALLOW_ORIGINS = ["http://localhost", "http://localhost:8080"]

LOG_LEVEL = "info"
LOG_FILE = "app.log"

# Email Settings for email service
EMAIL_SENDER = "berk@example.com"
EMAIL_PASSWORD = "SomeStrong_Password!@"
SMTP_SERVER = ""
SMTP_PORT = 1111
