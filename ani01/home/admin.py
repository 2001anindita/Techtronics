from django.contrib import admin
from home.models import *
from home1.models import userupload

admin.site.register(Quora)
admin.site.register(userupload)
admin.site.register(question)
admin.site.register(answer)
admin.site.register(comment)

