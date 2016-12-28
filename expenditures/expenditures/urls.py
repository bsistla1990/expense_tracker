

from django.conf.urls import url, include
from django.contrib import admin

from .routers import router


urlpatterns = [
    url(r'api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),

]
