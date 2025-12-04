import faker;
import random;
names = ["Олександр", "Марія", "Іван",
         "Софія", "Дмитро", "Анна", "Володимир", 
         "Олена", "Сергій", "Катерина", "Андрій", 
         "Вікторія", "Богдан", "Наталія", "Юрій", "Ірина"]
surnames = ["Коваленко", "Шевченко", "Мельник",
             "Бондар", "Ткачук", "Кравченко",
             "Олійник", "Савченко", "Гончаренко",
             "Лисенко", "Козак", "Романенко"]
with open("seeds.sql", 'w',encoding='utf-8') as f:
    f.write("INSERT INTO students (name, surname,age)VALUES\n")
    generatornamber = 1000
    for i in range(generatornamber):
        name = random.choice(names)
        surname = random.choice(surnames)
        age = random.randint(18, 60)
        f.write(f"('{name}', '{surname}', {age})")
        if i < generatornamber - 1:
            f.write(",\n")
        else:
            f.write(";\n")
print("Файл seeds.sql створено!")