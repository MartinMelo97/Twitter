from django.db import models 
from django.contrib.auth.models import User

class Twixt(models.Model):

	usuario = models.ForeignKey(User, related_name="blog_posts",blank=True,null=True)
	nombre_user= models.CharField(max_length=50)
	#titulo = models.CharField(max_length=100)
	cuerpo = models.TextField()
	fecha = models.DateField(auto_now=True)
	#actualizado = models.DateField(auto_now_add=True,blank=True,null=True)
	#status = models.CharField(max_length=10, choices=STATUS_CHOICES,default='draft',blank=True,null=True)
	slug = models.SlugField(max_length=200,unique_for_date='creado',blank=True,null=True)

	class Meta:
		orderin = ('-creado',)

	def __str__(self):
		return self.cuerpo