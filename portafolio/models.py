from django.db import models

# Create your models here.
class projecto(models.Model):
	
	titulo = models.CharField(max_length=200,blank=False)
	descripcion = models.TextField(blank=True,null=True)
	imagen = models.ImageField(blank = True,upload_to='projectos')
	creacion = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
	actualizacion = models.DateTimeField(auto_now=True,verbose_name="Ultima Actualizacion")
	url = models.URLField(verbose_name="direccion web",blank=True,null=True)

	class Meta:

		verbose_name ='Projecto'
		verbose_name_plural ='Projectos'
		# ordena por fecha de creacion desde el mas actual hasta el ultimo
		ordering =['-creacion']
	# metodo que muestra el titulo de un objeto
	def __str__(self):
		return self.titulo