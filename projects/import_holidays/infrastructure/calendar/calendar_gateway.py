from projects.import_holidays.infrastructure.calendar.calendar_client import CalendarClient

constants = {
    'year': 2021,
    'city': 'Sao_Paulo',
    'state': 'SP'
}


class CalendarGateway:

    def __init__(self, calendar_client: CalendarClient):
        self.calendar_client: CalendarClient = calendar_client

    def list(self):
        return self.calendar_client.list(params=constants)
