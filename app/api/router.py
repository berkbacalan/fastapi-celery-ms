from fastapi import FastAPI
from . import patrons, books, checkout

app = FastAPI()

app.include_router(patrons.router, prefix="/patron", tags=["patrons"])
app.include_router(books.router, prefix="/book", tags=["books"])
app.include_router(checkout.router, prefix="/checkout", tags=["checkout"])


async def startup_event():
    print("Application startup")


app.add_event_handler("startup", startup_event)
