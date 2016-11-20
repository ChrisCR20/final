# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class proyecto(models.Model):
	name = models.CharField(max_length = 60)

class tarea(models.Model):
	name = models.CharField(max_length = 60)
	user = models.ForeignKey(User, blank=True, null=True)
	creation_date =  models.DateTimeField(auto_now_add = True)
	finalization_date = models.DateTimeField(null = True, blank = True)
	priority = models.PositiveSmallIntegerField(default = 0)
	difficulty = models.PositiveSmallIntegerField(default = 0)
	project = models.ForeignKey(proyecto, null = True, blank = True)

	def set_done(self):
		self.finalization_date = datetime.now()

	def set_open(self):
		self.finalization_date = None

	def priority_str(self):
		if self.priority == 0:
			return "Baja"

		if self.priority == 1:
			return "Normal"

		if self.priority == 2:
			return "Alta"

		return "Sin definir"

	def difficulty_str(self):
		if self.difficulty == 0:
			return u"Muy fácil"

		if self.difficulty == 1:
			return u"Fácil"

		if self.difficulty == 2:
			return u"Normal"

		if self.difficulty == 3:
			return u"Difícil"

		if self.difficulty == 4:
			return u"Muy difícil"

		return "Sin definir"

	def project_str(self):
		if self.project == None:
			return "Sin definir"

		return self.project.name

	def user_str(self):
		if self.user == None:
			return "Todo el mundo"

		return self.user.username
