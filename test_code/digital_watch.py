# преобразовать произвольное число минут (возможно, более 1 суток) в показания цифровых часов
"""
переименовать по-питоновски модуль и идентификаторы
- [x] выполнено
в Python преимущественно используется нотация under_score

"""
"""
создать дополнительные строковые объекты с применением:
  - [x] f-строк
  - [x] функции format
  - [x] %

"""

total_minutes = int(12305)

watch_minutes = total_minutes % 60
full_days = total_minutes // (60*24)
watch_hours = (total_minutes // 60) - (full_days*24)

# добавлена добивка нулями слева
s_watch_hours = str(watch_hours).rjust(2, "0")
s_watch_minutes = str(watch_minutes).rjust(2, "0")
actual = s_watch_hours + ':' + s_watch_minutes
print(actual)

# f-string
actual_2 = f"{s_watch_hours}:{s_watch_minutes}"
print(actual_2)

# format
actual_3 = "{0}:{1}".format(s_watch_hours, s_watch_minutes)
print(actual_3)

# %
actual_3 = "%s:%s" % (s_watch_hours, s_watch_minutes)
print(actual_3)

# tuple (кортеж)
actual_tuple = (s_watch_hours, ":", s_watch_minutes)
for count in range(3):
    print(actual_tuple[count], end="")
"""
expected = "13:05"
assert actual == expected
print("Test passed")

expected = "13:35"
assert actual == expected
print("Test passed")
"""
