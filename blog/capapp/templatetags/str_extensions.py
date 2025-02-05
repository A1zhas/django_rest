from django import template

register = template.Library()

@register.filter
def capitalize(value):
    """Возвращает строку с заглавной первой буквой"""
    return value.capitalize() if isinstance(value, str) else value

@register.filter
def superoutput(inputstr):
    """Преобразует строку в чередующийся верхний/нижний регистр"""
    if not isinstance(inputstr, str):  # Проверка типа
        return inputstr
    return ''.join([inputstr[i].upper() if i % 2 == 0 else inputstr[i] for i in range(len(inputstr))])
