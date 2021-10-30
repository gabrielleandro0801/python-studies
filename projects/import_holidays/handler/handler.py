from projects.import_holidays.infrastructure.logger.log import logger
from projects.import_holidays.application.febraban_holiday_application_service import configure_application_service, \
    FebrabanHolidayApplicationService


def main(event, context):
    logger.info({"event": "handler", "detail": "Application started its job"})
    application_service: FebrabanHolidayApplicationService = configure_application_service()
    application_service.import_holidays()

    logger.info({"event": "handler", "detail": "Application finished its job"})


if __name__ == '__main__':
    main('', '')
