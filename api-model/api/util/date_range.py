from datetime import date, timedelta

class Date_Range():
    def __init__(self) -> None:
        self.date = date.today()

    def get_date_range(self, count: int) -> list[str]:
        """mendapatkan range tanggal dari hari ini sampai (count) hari"""
        return [str(self.date + timedelta(days=i))
                for i in range(count)]
