from django.contrib import admin
from post.models import Post 


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

	list_display = ('id', 'author', 'title', 'content', 'updated_at')
	"""@admin.display(empty_value='???')
	def content(self, obj):
		return obj.content"""

#admin.site.register(Post, PostAdmin)