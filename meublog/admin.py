from django.contrib import admin

# criando a tela de POSTS no painel admin
from .models import Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created", "update")
    #list_display = ("title", "slug", "author", "created")
    prepopulated_fields = {"slug": ("title",)}  # Preenche o SlUG automaticamente
# finalizando a criação do painel

