from django.db import models
from django.contrib import admin

class Contactus(models.Model):
    user = models.CharField(max_length=40, default='')
    tm = models.DateTimeField(editable=False)
    feedback = models.TextField(help_text="Your feedback is valuable to us.")

    @admin.display(description="Short feedback")
    def shortfeedback(self):
        return self.feedback[:20]


class ContactusAdmin(admin.ModelAdmin):
    list_display = ["tm","user", "shortfeedback"]


admin.site.register(Contactus, ContactusAdmin)