from django.contrib import admin
from .models import CustomUser, Post, Comment, SubComment, Like, LikeComment, Saved

admin.site.register(CustomUser)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(SubComment)
admin.site.register(Like)
admin.site.register(LikeComment)
admin.site.register(Saved)