from rest_framework import viewsets, filters
from .models import httpdinstance 
from .serializers import httpdinstanceSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class httpdinstanceViewSet(viewsets.ModelViewSet):
    queryset = httpdinstance.objects.all()
    serializer_class = httpdinstanceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (filters.SearchFilter,)
    #search_fields = ( 'apache_ciname', 'apache_appname', 'apache_server', 'apache_vipurl', 'apache_instance_group', 'apache_user', 'apache_httpd_version', 'apache_httpdswitch', 'apache_initscript', 'apache_apachescript', 'apache_listen_hostport', 'apache_environment', 'apache_AppDL', 'apache_Appowner', 'apache_comments', 'apache_giturl', 'apache_active' )
    search_fields = ( 'apache_ciname' , 'apache_appname' , 'apache_server' , 'apache_vipurl' , 'apache_instance_group' , 'apache_user' , 'apache_httpd_version' , 'apache_httpdswitch' , 'apache_initscript' , 'apache_apachescript' , 'apache_listen_hostport' , 'apache_environment' , 'apache_AppDL' , 'apache_Appowner' , 'apache_comments' , 'apache_datacenter' , 'apache_OS' , 'apache_OSver' , 'apache_giturl' , 'apache_active' ) 
