import holidays
from datetime import date, timedelta
from ..util.date_range import Date_Range



class Get_Holiday(Date_Range):
    def __init__(self) -> None:
        self.date = date.today()
        self.year = date.today().year

    def get_holiday(self):
        # Buat objek Holidays dengan kode "ID" yang merupakan kode negara untuk Indonesia
        holiday = holidays.Indonesia(years=self.year)
        id_holidays = holidays.CountryHoliday('ID')

        # Mendapatkan daftar hari libur akhir pekan
        weekend_holidays = []

        # Iterasi melalui setiap tanggal dalam rentang tahun
        start_date = date(self.year, 1, 1)
        end_date = date(self.year, 12, 31)

        while start_date <= end_date:
            # Periksa apakah tanggal adalah hari Minggu
            if start_date.weekday() == 6:  # 6 mewakili hari Minggu
                weekend_holidays.append(start_date)

            start_date += timedelta(days=1)

        # Tambahkan hari libur akhir pekan ke dalam objek holiday
        for holiday in weekend_holidays:
            id_holidays[holiday] = "Weekend Holiday"
        return id_holidays

    def get_holiday_range(self, count: int) -> list[int]:
        holidays = self.get_holiday()
        # jika libur berikan output 1 dan jika tidak output 0
        output = []
        for date in self.get_date_range(count):
            if date in holidays:
                output.append(1)
            else:
                output.append(0)

        return output
