from celery import Celery
from celery.schedules import crontab

from app.core.services.checkout_service import get_checkout_by_id, get_checked_out_books
from app.core.services.email_service import send_email
from app.core.services.patron_service import get_patron_by_id

from config.settings import CELERY_BROKER_URL
from database.database import SessionLocal

celery_app = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_BROKER_URL)
celery_app.conf.enable_utc = True
celery_app.conf.timezone = 'UTC'


@celery_app.task()
def send_reminder_email(checkout_id):
    db = SessionLocal()
    checkout = get_checkout_by_id(db, checkout_id)
    patron = get_patron_by_id(db, checkout.patron_id)
    patron_email = patron.email
    send_email(patron_email, "Checkout Reminder", f"Your book with id: {checkout.book_id} is overdue!")


@celery_app.task()
def generate_weekly_report():
    db = SessionLocal()
    checkouts = get_checked_out_books(db)
    report = f"Report Success:Checkout Count: {len(checkouts)}"
    print(report)


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour="08", minute="30", day_of_week="1"),
        generate_weekly_report.s(),
    )
