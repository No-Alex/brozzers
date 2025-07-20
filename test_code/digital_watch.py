# преобразовать произвольное число минут (возможно, более 1 суток) в показания цифровых часов
# TODO - переименовать по-питоновски модуль и идентификаторы
# выполнено
# В Python преимущественно используется нотация under_score
total_minutes = int(12305)

watch_minutes = total_minutes % 60
full_days = total_minutes // (60*24)
watch_hours = (total_minutes // 60) - (full_days*24)
# добавить добивку нулями слева
# s_watch_hours = "0" + str(watch_hours)
# s_watch_hours = s_watch_hours[-2:]
# замена на .rjust()
s_watch_hours = str(watch_hours).rjust(2, "0")
# s_watch_minutes = "0" + str(watch_minutes)
# s_watch_minutes = s_watch_minutes[-2:]
# замена на .rjust()
s_watch_minutes = str(watch_minutes).rjust(2, "0")
actual = s_watch_hours + ':' + s_watch_minutes
print(actual)
"""
строка 14 - создать дополнительные строковые объекты с применением:
  - [x] f-строк
  - [x] функции format
  - [x] %
"""
# f-string
actual_2 = f"{s_watch_hours}:{s_watch_minutes}"
print(actual_2)

# format
actual_3 = "{0}:{1}".format(s_watch_hours, s_watch_minutes)
print(actual_3)

# %
actual_3 = "%s:%s" % (s_watch_hours, s_watch_minutes)
print(actual_3)

"""
expected = "13:05"
assert actual == expected
print("Test passed")

expected = "13:35"
assert actual == expected
print("Test passed")
"""
