from models.BaseModel import BaseModel
from models.BookingDatesModel import BookingDatesModel


class BookingModel(BaseModel):
    def __init__(self,
                 first_name="Jim",
                 last_name="Brown",
                 total_price=111,
                 deposit_paid=True,
                 booking_dates=None,
                 additional_needs="Breakfast"
                 ):
        self.firstname = first_name
        self.lastname = last_name
        self.totalprice = total_price
        self.depositpaid = deposit_paid
        self.bookingdates = booking_dates
        if booking_dates is None:
            self.bookingdates = BookingDatesModel()
        else:
            self.booking_dates = booking_dates
        self.additionalneeds = additional_needs
        super().__init__()
