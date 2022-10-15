# Algoritmix_task_1_sprint
Решение двух алгоритмических задач с сервиса Яндекс.Контест
#Задача_1:
A. Ближайший ноль
Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
Все языки	3 секунды	256Mb	стандартный ввод или input.txt	стандартный вывод или output.txt
Golang 1.14.4 + network	0.8 секунд	64Mb
Node.js 14.15.5	1.6 секунд	256Mb
C# (MS .Net 5.0)+ASP	1.6 секунд	400Mb
gc go	0.8 секунд	64Mb
Oracle Java 8	1.6 секунд	400Mb
OpenJDK Java 11	1.6 секунд	400Mb
Golang 1.16	0.8 секунд	64Mb
GNU c++17 7.3	0.8 секунд	64Mb
Node JS 8.16	1.6 секунд	256Mb
Тимофей ищет место, чтобы построить себе дом. Улица, на которой он хочет жить, имеет длину n, то есть состоит из n одинаковых идущих подряд участков. Каждый участок либо пустой, либо на нём уже построен дом.

Общительный Тимофей не хочет жить далеко от других людей на этой улице. Поэтому ему важно для каждого участка знать расстояние до ближайшего пустого участка. Если участок пустой, эта величина будет равна нулю — расстояние до самого себя.

Помогите Тимофею посчитать искомые расстояния. Для этого у вас есть карта улицы. Дома в городе Тимофея нумеровались в том порядке, в котором строились, поэтому их номера на карте никак не упорядочены. Пустые участки обозначены нулями.

Формат ввода
В первой строке дана длина улицы —– n (1 ≤ n ≤ 106). В следующей строке записаны n целых неотрицательных чисел — номера домов и обозначения пустых участков на карте (нули). Гарантируется, что в последовательности есть хотя бы один ноль. Номера домов (положительные числа) уникальны и не превосходят 109.

Формат вывода
Для каждого из участков выведите расстояние до ближайшего нуля. Числа выводите в одну строку, разделяя их пробелами.
__________________________________________________________________________________________________________________________________________________________
#Задача_2:
B. Ловкость рук
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Игра «Тренажёр для скоростной печати» представляет собой поле из клавиш 4x4. В нём на каждом раунде появляется конфигурация цифр и точек. На клавише написана либо точка, либо цифра от 1 до 9.

В момент времени t игрок должен одновременно нажать на все клавиши, на которых написана цифра t. Гоша и Тимофей могут нажать в один момент времени на k клавиш каждый. Если в момент времени t нажаты все нужные клавиши, то игроки получают 1 балл.

Найдите число баллов, которое смогут заработать Гоша и Тимофей, если будут нажимать на клавиши вдвоём.



Формат ввода
В первой строке дано целое число k (1 ≤ k ≤ 5).

В четырёх следующих строках задан вид тренажёра –— по 4 символа в каждой строке. Каждый символ —– либо точка, либо цифра от 1 до 9. Символы одной строки идут подряд и не разделены пробелами.

Формат вывода
Выведите единственное число –— максимальное количество баллов, которое смогут набрать Гоша и Тимофей.

Пример 1
Ввод	Вывод
3
1231
2..2
2..2
2..2
2
Пример 2
Ввод	Вывод
4
1111
9999
1111
9911
1
Пример 3
Ввод	Вывод
4
1111
1111
1111
1111
0