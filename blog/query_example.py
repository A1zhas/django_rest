# python manage.py shell

# Основные
# all, get, filter
# 1. с одним параметром
# Post.objects.filter(name='tank')
# 2. exclude = фильтр наоборот
# Post.objects.exclude(name='tank')
# 3. Несколько параметров
# Post.objects.filter(name='tank', text='ddd')
# Можно применять любые запросы к полученному QuerySet
# In [11]: tanks = Post.objects.filter(name='tank')
# In [12]: some = tanks.filter(text='ddd')
# In [13]: some
# Out[13]: <QuerySet []>

# tanks = Post.objects.filter(name='tank').filter(text='ddd').filter(name='ggg')
# tanks = Post.objects.filter(name='tank').exclude(text='ddd')

# Сложные фильтры
# 1. больше меньше (например найти все посты с рейтингом больше 3)
# Post.objects.filter(rating__gt=3)
# Post.objects.filter(rating__lt=3)
# Post.objects.filter(rating__gte=3)
# Post.objects.filter(rating__lte=3)

# 2. Посты с рэйтингом 2 или 3
# Post.objects.filter(rating__gte=3, rating__lte=4)
# 3. Посты начинаютя (name) на ta..
# Post.objects.filter(name__startswith='ta')
# 4. Посты в имени котрых есть nk, ...nk...
# Post.objects.filter(name__contains='nk')
# 5. Посты с датой создания меньше какой-то
# In [13]: import datetime
# In [14]: somedate = datetime.datetime(year=2000, month=1, day=1)
# In [15]: Post.objects.filter(create__gt=somedate)

# Post.objects.filter(create__year=2000, create__day=1, create__month=1)

# 6. Запросы к связанным моделям
# Задача 1. Получить посты с категорией у которой имя cars
# Вариант 'на python'
# In [18]: cars = Category.objects.get(name='cars')
# In [19]: Post.objects.filter(category=cars)
# Вариант 'на ORM'
# Post.objects.filter(category__name='cars')
# Goods.objects.filter(shop__city__country__president__wife__name='Kate')

# Задача 2. Получить посты с категорией у которой имя начинается на ca...
# Post.objects.filter(category__name__startswith='ca')