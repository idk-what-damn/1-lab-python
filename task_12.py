def calculate_mobile_bill():
    # Базовые параметры тарифа
    base_minutes = 60
    base_sms = 30
    base_data_mb = 1024  # 1 ГБ = 1024 МБ
    base_price = 24.99

    # Стоимость дополнительных услуг
    extra_minute_price = 0.89
    extra_sms_price = 0.59
    extra_mb_price = 0.79
    tax_rate = 0.02

    # Ввод данных от пользователя
    minutes_used = int(input("Введите количество использованных минут: "))
    sms_used = int(input("Введите количество отправленных SMS: "))
    data_used_mb = int(input("Введите объём интернет-трафика в МБ: "))

    # Расчёт перерасхода
    extra_minutes = max(0, minutes_used - base_minutes)
    extra_sms = max(0, sms_used - base_sms)
    extra_data_mb = max(0, data_used_mb - base_data_mb)

    # Стоимость дополнительных услуг
    extra_minutes_cost = extra_minutes * extra_minute_price
    extra_sms_cost = extra_sms * extra_sms_price
    extra_data_cost = extra_data_mb * extra_mb_price

    # Общая сумма до налога
    subtotal = base_price + extra_minutes_cost + extra_sms_cost + extra_data_cost

    # Налог
    tax = subtotal * tax_rate

    # Итоговая сумма
    total = subtotal + tax

    # Вывод
    print("\nБазовая сумма тарифа:", base_price, "руб.")
    if extra_minutes > 0:
        print("Дополнительные минуты: ", extra_minutes, extra_minutes_cost, "руб.")
    if extra_sms > 0:
        print("Дополнительные SMS: ", extra_sms,  extra_sms_cost, "руб.")
    if extra_data_mb > 0:
        print("Дополнительный интернет: ", extra_data_mb, "МБ ", extra_data_cost, "руб.")
    print("Налог (2%): ", tax, " руб.")
    print("Итоговая сумма к оплате: ", total, "руб.")

calculate_mobile_bill()
