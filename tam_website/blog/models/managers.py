from django.db import models


class ArticleManager(models.Manager):

    def accepted(self):
        return self.filter(status='AC')
    
