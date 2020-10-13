from django.contrib import admin
from Bryggelogg.models import Bryggelogg, Recipes, Malt, Hop

# Register your models here.
admin.site.register(Bryggelogg)
admin.site.register(Recipes)
admin.site.register(Malt)
admin.site.register(Hop)
