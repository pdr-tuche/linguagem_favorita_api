
from rest_framework import routers
from .views import PessoaViewSet

router = routers.DefaultRouter()

router.register(r'', PessoaViewSet)

urlpatterns = router.urls
