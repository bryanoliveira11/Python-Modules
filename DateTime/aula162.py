from datetime import datetime

# from pytz import timezone

# data = datetime(2022, 4, 20, 7)
# data_str_data = "2022-04-20 7:49:23"
# data_str_fmt = "%Y-%m-%d %H:%M:%S"
# data_f = datetime.strptime(data_str_data, data_str_fmt)

# data = datetime.now((timezone('Asia/Tokyo')))

data = datetime.now()

print(data.timestamp())
print(datetime.fromtimestamp(data.timestamp()))
