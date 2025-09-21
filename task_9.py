print("Введите ваш IP адрес вида ХХХ.ХХХ.ХХХ.ХХХ, где ХХХ – число от 0 до 255: ")

ip_string = input().strip()

if not ip_string.strip():
    print("Строка пустая!")

parts = ip_string.split(".")
if (len(parts) == 4 and
    parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit() and parts[3].isdigit() and
    0 <= int(parts[0]) <= 255 and
    0 <= int(parts[1]) <= 255 and
    0 <= int(parts[2]) <= 255 and
    0 <= int(parts[3]) <= 255):
    print(" Правильный IP-адрес!")
else:
    print(" Неправильный IP-адрес!")