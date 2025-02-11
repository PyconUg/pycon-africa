import os
import django
from home.models import EventYear

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pyconafrica.settings")
django.setup()

event_year = EventYear.objects.create(year=2030, home_info="This is the 2020 event year", template_path="home/2020/home.html")
event_year.save()
print("Event Year created successfully")
