from django.db import models

#
# Status = (
#     ('Оформлен', 'Оформлен'),
#     ('Отменен', 'Отменен'),
#     ('Новый', 'Новый')
# )

# class User_information(models.Model):
#     name = models.CharField(max_length=200, null=True, blank=True, verbose_name='Имя')
#     last_name = models.CharField(max_length=200, blank=True, null=True,
#                                  verbose_name='Фамилия')
#     mail = models.CharField(max_length=200, blank=True, null=True,
#                             verbose_name='Почта')
#     num = models.CharField(max_length=50, blank=True, null=True,
#                            verbose_name='Номер')
#     country = models.CharField(max_length=100, null=True, blank=True,
#                                verbose_name='Страна')
#     city = models.CharField(max_length=100, null=True, blank=True,
#                             verbose_name='Город')
#     date_order = models.CharField(max_length=50, null=True, blank=True,
#                                   verbose_name='Дата оформления заказа')
#     status = models.CharField(choices=Status, max_length=300, db_index=True,
#                               default=('Новый', 'Новый'), verbose_name='Выбор из списка')
#
#     def __str__(self):
#         return self.name
#
#

