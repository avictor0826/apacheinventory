from django.db import models

# Create your models here.
#class Article(models.Model):
#    article_id = models.AutoField(primary_key=True)
#    article_heading = models.CharField(max_length=250)
#    article_body = models.TextField()

class httpdinstance(models.Model):
    apache_id = models.AutoField(primary_key=True)
    apache_ciname = models.CharField(max_length=250)
    apache_appname = models.CharField(max_length=250)
    apache_server = models.CharField(max_length=250)
    apache_vipurl = models.CharField(max_length=250)
    apache_instance_group = models.CharField(max_length=250)
    apache_user = models.CharField(max_length=250)
    apache_httpd_version = models.CharField(max_length=250)
    apache_httpdswitch = models.CharField(max_length=250,blank=True)
    apache_initscript = models.CharField(max_length=250)
    apache_apachescript = models.CharField(max_length=250)
    apache_listen_hostport = models.CharField(max_length=250)
    apache_environment = models.CharField(max_length=250,default='DEV')
    apache_AppDL = models.CharField(max_length=250,default='NA',blank=True)
    apache_Appowner = models.CharField(max_length=250,default='NA',blank=True)
    apache_comments = models.TextField(blank=True)
    apache_datacenter = models.CharField(max_length=250)
    apache_OS = models.CharField(max_length=250)
    apache_OSver = models.CharField(max_length=250,default='NA',blank=True)
    apache_giturl = models.CharField(max_length=250,default='NA',blank=True)
    apache_active = models.BooleanField(default=True)
