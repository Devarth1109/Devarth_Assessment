from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	pswd = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Member(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	m_name = models.CharField(max_length=100)
	m_contact = models.CharField(max_length=100)
	m_num = models.CharField(max_length=100)

	def __str__(self):
		return self.m_name +" - "+self.m_contact+" - "+self.m_num

class Chairman(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	c_name = models.CharField(max_length=100)
	c_contact = models.CharField(max_length=100)

	def __str__(self):
		return self.c_name +" - "+self.c_contact

class Watchman(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	w_name = models.CharField(max_length=100)
	w_contact = models.CharField(max_length=100)

	def __str__(self):
		return self.w_name +" - "+self.w_contact

class Visitors(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	v_name = models.CharField(max_length=100)
	v_contact = models.CharField(max_length=100)

	def __str__(self):
		return self.v_name +" - "+self.v_contact

class Event(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	e_name = models.CharField(max_length=100)
	e_date = models.CharField(max_length=100)

	def __str__(self):
		return self.e_name +" - "+self.e_date

class Notice(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	n_name = models.CharField(max_length=100)
	n_sub = models.CharField(max_length=100)

	def __str__(self):
		return self.n_name +" - "+self.n_sub