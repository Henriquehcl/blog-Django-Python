from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)  # titulo da postagem
    slug = models.SlugField(max_length=255, unique=True)  # endereço da postagem, URI
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # captura o autor da postagem
    body = models.TextField()  # texto da postagem
    created = models.DateTimeField(auto_now_add=True)  # adiciona a data/hora automaticamente
    update = models.DateTimeField(auto_now=True)  # atualiza a data conforme atualizações do post
    #status. criar um campo de status!!!!  
    
    # fazendo a ordenação das postagens da mais recente para mais antiga
    class Meta:
        ordering = ('-created',) 

    # corrigindo o título do post no painel admin, onde originalmente fica
    # Post Objet ficará no titulo do post
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug }) # definindo a URL da postagem    