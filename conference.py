print("Welcome to our Conference Hall!")

#This is the new comment added by me.
tickets = list(map(int, input("How many tickets do you want to buy?: ")))
age = list(map(int, input("Please, enter the age of each person with space: ").split()))

# Объявляем пустую переменную-счётчик (total_sum) и циклом for-in проходим по листу возрастов (age) для определения стоимости билета;

total_sum = 0
for item in age:
    if item < 18:
        total_sum = 0
    elif 18 < item < 25:
        total_sum += 990
    elif item > 25:
        total_sum += 1390
    else:
        print("Sorry, something went wrong. Try again.")
		
# Для подсчёта 10-ти процентной скидки вводим новую переменную discount(скидка), которая вычитает процент и выводит на экран конечную сумму, 
# пройдя по списку количества покупаемых билетов (tickets);
per_cent = (total_sum / 100) * 10
discount = total_sum - per_cent
for item in tickets:
    if item > 3:
        print(f"Your total bill is {discount} rubles.")
    elif item < 3:
        print(f"Your total bill is {total_sum} rubles.")
    else:
        print("Sorry, something went wrong. Try again.")
