from django.contrib import admin
from .models import IrregularVerbs, Letter, Fiche


class IrregularVerbsInline(admin.TabularInline):
    model = IrregularVerbs
    extra = 1


class LetterAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Lettre', {'fields': ['letter']})
    ]
    inlines = [IrregularVerbsInline]

    class Meta:
        ordering = ['letter']


admin.site.register(Letter, LetterAdmin)
admin.site.register(IrregularVerbs)
admin.site.register(Fiche)
