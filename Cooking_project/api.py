from rest_framework import routers
from calories import views as calories_v

router = routers.DefaultRouter()
router.register(r'calories', calories_v.IngredientsViewset)
