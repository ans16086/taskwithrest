from django.db import models


from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
# Create your models here.







class userprofilee(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
   
    addressUser =models.TextField(verbose_name=_("Address"))
    def __str__(self) -> str:
         return f"{self.user.username}: {self.addressUser}"
                                            



class deletebutton(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    deleteq=models.BooleanField(default=False)