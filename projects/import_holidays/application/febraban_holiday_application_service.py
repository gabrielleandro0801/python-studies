from projects.import_holidays.domain.holiday_service import HolidayService


class FebrabanHolidayApplicationService:

    def __init__(self, holiday_service: HolidayService):
        self.holiday_service = holiday_service

    def import_holidays(self):
        self.holiday_service.list_holidays()
