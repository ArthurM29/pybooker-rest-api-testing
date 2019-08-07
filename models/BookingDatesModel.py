from models.BaseModel import BaseModel


class BookingDatesModel(BaseModel):
    def __init__(self,
                 checkin="2018-01-01",
                 checkout="2018-01-14"
                 ):
        self.checkin = checkin
        self.checkout = checkout
        super().__init__()
