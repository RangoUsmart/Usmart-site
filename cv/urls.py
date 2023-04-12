#users/urls.py
"""
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from . import views
# from projects import views as v2

app_name = 'rezume' 
urlpatterns = urlpatterns = [
    path('', views.RezumeView.as_view(), name='cv'),
    path('edit/', views.cv_edit, name='cv_edit'),
]

