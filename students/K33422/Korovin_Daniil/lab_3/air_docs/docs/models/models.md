# Описание моделей данных

Информация о "проектировании" модели, описание итоговой "базы данных"

## Работник
Worker(AbstractUser):

    id = primary_key, индивидуален и уникален, создаётся автоматически
    fio = фио работника (будет "возвращаться")
    age = возраст (по умолчанию 18)

    education_types = (
        ('VSH', "Высшее"),
        ('VSN', "Высшее неоконченное"),
        ('SRD', "Среднее"),
        ('SRS', "Среднее специальное"),
    )
    education = выбор из уровней образования. Это минимальные значения, с которыми
    принимают в компанию
    stajh_raboty = стаж работы
    passport = данные паспорта

## Экипаж
Ekipazh(models.Model):

    id = primary_key, индивидуален и уникален, создаётся автоматически
    name = название экипажа (будет "возвращаться")

## Авиакомпания 
Aviacompany(models.Model):

    id_ekipazha = foreignKey от "Экипажа" 
    id_workera = foreignKey от "Работника"
    work = занимаемая должность
    
## Самолёт
Plane(models.Model):
    
    id = primary_key, индивидуален и уникален, создаётся автоматически
    type = тип модели (будет "возвращаться")
    number = номер модели (будет "возвращаться")
    mesta = количество мест
    speed = скорость полёта
    avia = авиакомпания (будет "возвращаться")

## Разрешение
Razrechenie(models.Model):

    id_plane = foreignKey от "Самолёта"
    id_ekipazha = foreignKey от "Экипажа"
    razrechenie = есть разрешение - да/нет?
    
## Ремонт
Remont(models.Model):
    
    id = primary_key, индивидуален и уникален, создаётся автоматически
    id_plane = foreignKey от "Самолёта"
    polomka = поломка
    
## Транзит 
Tranzit(models.Model):

    id = primary_key, индивидуален и уникален, создаётся автоматически
    punkt_peresadki = пересадка (будет "возвращаться")
    
## Рейс
class Reys(models.Model):

    number = primary_key, индивидуален и уникален (будет "возвращаться")
    distance = расстояние до пункта назначения
    punkt_start = пункт вылета (будет "возвращаться")
    punkt_end = пункт прилёта (будет "возвращаться")
    id_tranzita = необязательный foreignKey от "Транзита"

## Допуск
Dopusk(models.Model):

    number_reysa = foreignKey от "Рейса"
    id_ekipazha = foreignKey от "Экипажа"
    nalichie_dopuska = есть допуск - да/нет?
    
## Полёт
Polet(models.Model):

    id_poleta = primary_key, индивидуален и уникален, создаётся автоматически
    number_reysa = foreignKey от "Рейса" (будет "возвращаться")
    id_plane = foreignKey от "Самолёта" (будет "возвращаться")
    date_start = дата вылета
    time_start = время вылета
    date_end = дата прилёта
    time_end = время прилёта
    sell_tickets = количество проданных билетов
    made_reys = количество совершённых рейсов
    date_start_tranzit = дата транзитной посадки (необязательно)
    time_start_tranzit = время транзитной посадки (необязательно)
    date_end_tranzit = дата вылета из транзита (необязательно)
    time_end_tranzit = время вылета из транзита (необязательно)
