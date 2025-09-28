base_minutes = 60
base_sms = 30
base_data_mb = 1024 
base_price = 24.99

extra_minute_price = 0.89
extra_sms_price = 0.59
extra_mb_price = 0.79
tax_rate = 0.02

minutes_used = int(input("Введите количество использованных минут: "))
sms_used = int(input("Введите количество отправленных SMS: "))
data_used_mb = int(input("Введите объём интернет-трафика в МБ: "))

if minutes_used > base_minutes:
    extra_minutes = minutes_used - base_minutes
else:
    extra_minutes = 0

if sms_used > base_sms:
    extra_sms = sms_used - base_sms
else:
    extra_sms = 0

if data_used_mb > base_data_mb:
    extra_data_mb = data_used_mb - base_data_mb
else:
    extra_data_mb = 0

extra_minutes_cost = extra_minutes * extra_minute_price
extra_sms_cost = extra_sms * extra_sms_price
extra_data_cost = extra_data_mb * extra_mb_price

subtotal = base_price + extra_minutes_cost + extra_sms_cost + extra_data_cost

tax = subtotal * tax_rate

total = subtotal + tax

print("\nБазовая сумма тарифа:", base_price, "руб.")
if extra_minutes > 0:
    print("Дополнительные минуты:", extra_minutes, "шт. →", extra_minutes_cost, "руб.")
if extra_sms > 0:
    print("Дополнительные SMS:", extra_sms, "шт. →", extra_sms_cost, "руб.")
if extra_data_mb > 0:
    print("Дополнительный интернет:", extra_data_mb, "МБ →", extra_data_cost, "руб.")
print("Налог (2%):", tax, "руб.")
print("Итоговая сумма к оплате:", total, "руб.")
