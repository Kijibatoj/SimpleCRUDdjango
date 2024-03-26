from rest_framework import routers
from .API import ProjectViewSet
router=routers.DefaultRouter()

router.register('api/ThonerProjects', ProjectViewSet, 'projects')

urlpatterns = router.urls