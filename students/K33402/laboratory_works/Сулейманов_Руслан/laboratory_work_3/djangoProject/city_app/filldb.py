import json
import os


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
    import django
    django.setup()
    from city_app.models import CityList

    with open('city.list.min.json', 'r', encoding='utf-8') as f:
        data = f.read()
    cities = json.loads(data)
    objects_list = []
    for city in cities:
        objects_list.append(
            CityList(city_cod=city['id'], name=city['name'], state=city['state'], country=city['country'],
                     coord_lon=city['coord']['lon'], coord_lat=city['coord']['lat']))
    CityList.objects.bulk_create(objects_list)


if __name__ == '__main__':
    main()
