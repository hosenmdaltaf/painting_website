from django.contrib import admin
from .models import Blog,Comment
from django_summernote.admin import SummernoteModelAdmin

# class Bloglist(admin.ModelAdmin):
#     summernote_fields = ('content')
#     list_display = ('title','writer','post_date','image_tag')


class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Blog,BlogAdmin)

admin.site.register(Comment)


# class PostAdmin(SummernoteModelAdmin):
#     summernote_fields = ('content',)

# admin.site.register(Post, PostAdmin)
