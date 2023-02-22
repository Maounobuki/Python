# Задание 16:
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке



frase = str(input('Введите кричалку:'))

frase = frase.split()





def VovelsInFraseCount(splitted_frase):

 vovels_set = ['а','у','о','и','ы','я','ю','ё','э','е','e','i','u','o','a']
 frases_vovels_counts = []
 for frase in splitted_frase:
  frase = frase.lower()
  count = 0
  for i in frase:
    if i in vovels_set:
       count += 1
  frases_vovels_counts.append(count)
 return frases_vovels_counts

counts_list = VovelsInFraseCount(frase)

setting = set(counts_list)

if len(setting) > 1:
                         print('Пам парам')
else:
                         print('Парам пам-пам')