from typing import List

from projects.import_holidays.domain.holiday import Holiday
from projects.import_holidays.domain.holiday_filter import HolidayFilter
from projects.import_holidays.infrastructure.calendar.calendar_gateway import CalendarGateway


class HolidayService:

    def __init__(self, calendar_gateway: CalendarGateway, holiday_filter: HolidayFilter):
        self.calendar_gateway: CalendarGateway = calendar_gateway
        self.holiday_filter = holiday_filter

    def list_febraban_holidays(self) -> List[Holiday]:
        holidays: List[Holiday] = self.calendar_gateway.list()
        holidays: List[Holiday] = list(filter(self.holiday_filter.check_type, holidays))
        return self.remove_duplication(holidays=holidays)

    def remove_duplication(self, holidays: List[Holiday]) -> List[Holiday]:
        clean_holidays = {}

        for holiday in holidays:
            if holiday.get_date() not in clean_holidays:
                clean_holidays[holiday.get_date()] = holiday

        return list(clean_holidays.values())
