class HolidayService:

    def __init__(self, calendar_gateway: CalendarGateway):
        self.calendar_gateway: CalendarGateway = calendar_gateway

    def list_holidays(self) -> None:
        self.calendar_gateway.list()