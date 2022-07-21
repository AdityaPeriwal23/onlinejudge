from django.contrib import admin

from .models import User,Problem,TestCases,Submissions

admin.site.register(User)
admin.site.register(Problem)
admin.site.register(TestCases)
admin.site.register(Submissions)
