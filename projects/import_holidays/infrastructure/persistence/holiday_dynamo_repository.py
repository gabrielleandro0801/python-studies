from typing import List
from projects.import_holidays.domain.holiday import Holiday


TABLE_NAME = 'report_ccs_holidays'


def translate_holiday_to_dynamo(holiday: Holiday):
    return holiday.to_json()


class HolidayDynamoRepository:

    def __init__(self, dynamo_client):
        self.dynamo_client = dynamo_client

    def save(self, holidays: List[Holiday]) -> None:
        table = self.dynamo_client.Table(TABLE_NAME)

        with table.batch_writer() as batch:
            for holiday in holidays:
                batch.put_item(
                    Item=translate_holiday_to_dynamo(holiday=holiday)
                )
