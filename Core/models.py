from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    login = models.CharField('Логин', unique=True, max_length=100)
    name = models.CharField(_('name'), max_length=30, blank=True)
    is_active = models.BooleanField(_('is_active'), default=True)
    is_staff = models.BooleanField(_('is_staff'), default=True)
    login_key = models.CharField('Ключ входа по бейджу', max_length=30, blank=True, unique=False)
    storeRole = models.CharField('Роль пользователя', max_length=100, default='none')
    backoffice_login = models.CharField('Ключ BackOffice', max_length= 100, default='none')
    bearer_token = models.CharField('Bearer Token пользователя', max_length=1000, default='none')
    
    # НАСТРОЙКИ ПОЛЬЗОВАТЕЛЯ
    #Принтеры
    selected_stationary_printer = models.CharField('Выбранный стационарный принтер', max_length=100, blank=True, null=True)
    selected_thermo_printer = models.CharField('Выбранный термопринтер', max_length=100, blank=True, null=True)
    selected_mobile_printer_yellow = models.CharField('Выбранный мобильный принтер с желтой бумагой', max_length=100, blank=True, null=True)
    selected_mobile_printer_white = models.CharField('Выбранный мобильный принтер с белой бумагой', max_length=100, blank=True, null=True)
    
    
    
    objects = UserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    def __str__(self):
        return self.name


class ErrorLog(models.Model):
    error_text = models.CharField('Ошибка', max_length=100)
    timestamp = models.DateTimeField('Дата и время ошибки', default= timezone.now)
    
    def __str__(self):
        return f'[{self.timestamp}] {self.error_text}'
    class Meta:
        verbose_name = 'ошибку'
        verbose_name_plural = 'ошибки'
        
        
class HeadMenu(models.Model):
    name = models.CharField('Наименование пункта', max_length=100)
    url = models.CharField('Ссылка (от корня)', max_length=100)
    title = models.BooleanField('Заголовок?', default=False)
    gk_name = models.CharField('Имя в GK', max_length=100)
    icon = models.CharField('Наименование иконки в GMD', max_length=100)
    index = models.CharField('Порядковый номер пункта', max_length=100, default='99')
    def __str__(self):
        if self.title:
            x = '👑 '
        else:
            x = ''
        return f'{x}[{self.gk_name}] {self.name}'
    class Meta:
        verbose_name = 'пункт'
        verbose_name_plural = 'пункты'
        ordering = ['index']
        
        
class DropMenu(models.Model):
    name = models.CharField('Наименование пункта', max_length=100)
    url = models.CharField('Ссылка (от корня)', max_length=100)
    headmenu = models.ForeignKey(HeadMenu, on_delete=models.CASCADE)
    gk_name = models.CharField('Имя в GK', max_length=100)
    icon = models.CharField('Наименование иконки в GMD', max_length=100)
    
    def __str__(self):
        return f'[{self.gk_name}] {self.name}'
    class Meta:
        verbose_name = 'пункт'
        verbose_name_plural = 'пункты'
    
    
class Label(models.Model):
    name = models.CharField(max_length=255)
    qr = models.CharField(max_length=255)
    appName = models.CharField(max_length=255)
    printer = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
