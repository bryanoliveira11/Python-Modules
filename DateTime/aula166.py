import calendar

# print(calendar.calendar(2023))
# print(calendar.month(2023, 6))
# num_primeiro_dia, ultimo_dia = calendar.monthrange(2023, 6)
# print(list(enumerate(calendar.day_name)))
# print(calendar.day_name[num_primeiro_dia])
# print(calendar.day_name[calendar.weekday(2023, 6, ultimo_dia)])

for week in calendar.monthcalendar(2023, 6):
    for day in week:
        if day == 0:
            continue
        print(day)
