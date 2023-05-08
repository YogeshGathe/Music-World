from django.contrib import admin
from api.models import Chord

# Register your models here.

@admin.register(Chord)
class ChordAdmin(admin.ModelAdmin):
    list_display= ['id', 'title', 'singer', 'chord']


