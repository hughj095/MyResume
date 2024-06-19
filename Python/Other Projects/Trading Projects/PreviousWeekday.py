from datetime import datetime, timedelta

class PreviousWeekday:
    def get_yesterday(self):
        today = datetime.now()
        yesterday = today - timedelta(days=1)
        if yesterday.weekday() < 5:
            return yesterday.strftime("%Y-%m-%d")
        else:
            friday = today - timedelta(days=(today.weekday() - 4) % 7)
            return friday.strftime("%Y-%m-%d")