from django.contrib import admin
from Bryggelogg.models import Bryggelogg, Recipes, Malt

# Register your models here.
admin.site.register(Bryggelogg)
admin.site.register(Recipes)
admin.site.register(Malt)
