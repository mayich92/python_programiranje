import datetime
import calendar
import string
from time import timezone

months = [name for name in calendar.month_name]
months = list(calendar.month_name)
# print(months)

trenutno = datetime.datetime.now()
trenutni_datum = datetime.date.today()
iz_timestampa = datetime.date.fromtimestamp(1593780000)
trenutni_mjesec = calendar.month_name[trenutno.month]
vrijeme1 = datetime.time(12, 45, 56)    # 12:45:56 u time obliku
vrijeme2 = datetime.time(hour=12, minute=45, second=56)    # 12:45:56 u time obliku
print(vrijeme1 == vrijeme2)
print(trenutno, trenutni_mjesec, vrijeme1, trenutni_datum, iz_timestampa)

t1 = datetime.datetime(2022, 4, 11, 1, 30)
t2 = datetime.datetime(year=2023, month=4, day=13, hour=2)
delta = t2-t1
print(delta)

print(trenutno.strftime('%d.%#m.%Y.    %H:%M %B %b'))    # crtica umjesto hashtaga u UNIX/macOS
print(trenutno.strftime("%Z"))

print(datetime.date.weekday(trenutni_datum))
petak = datetime.date(2023, 4, 14)
print(datetime.date.weekday(petak))

string_datum = "11.04.2023."
datum = datetime.datetime.strptime(string_datum, "%d.%m.%Y.")
print(datum)


# # vremenske zone
# from dateutil import tz
# tz_zg = tz.gettz('Europe/Zagreb')
# termin_zg = datetime.datetime(2021, 3, 29, tzinfo=tz_zg)

# tz_ny = tz.gettz('America/New_York')
# termin_ny = termin_zg.astimezone(tz_ny)

# tz_la = tz.gettz('America/Los_Angeles')
# termin_la = termin_zg.astimezone(tz_la)

# tz_hk = tz.gettz('Asia/Hong_Kong')
# termin_hk = termin_zg.astimezone(tz_hk)