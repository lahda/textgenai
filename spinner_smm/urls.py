from django.urls import include, path
from recordings.views import sauvegarder_contenu_rewrite,sauvegarder_contenu_extends,sauvegarder_contenu_summary
from spinner.views import  generate_summary,chat_completion,generate_rewrite,extend_content,home,home1
from show.views import affichage
from delete.views import delete_summary,supprimer_enregistrement_ext,delete_rewrite
from django.contrib import admin
from auths.views import logine,signup,mpd,deconnexion 


urlpatterns = [
    path('delete_rewrite/', delete_rewrite, name='delete_rewrite'),
    path('delete_summary/', delete_summary, name='delete_summary'),
    path('supprimer_enregistrement_ext/', supprimer_enregistrement_ext, name='supprimer_enregistrement_ext'),
    
    path('toutenregistrement/', affichage, name='toutenregistrement'),
    path('enregistrements/', sauvegarder_contenu_rewrite, name='enregistrements'),
    path('enregistrementsextends/', sauvegarder_contenu_extends, name='enregistrementsextends'),
    path('enregistrementsummary/', sauvegarder_contenu_summary, name='enregistrementsummary'),
    
    path('deconnexion/', deconnexion, name="deconnexion"),
    path('mpd/', mpd, name="mpd"),
    path('signup/', signup, name="signup"),
    path('login/', logine, name="login"),
    path('home/', home, name="home"),
     path('home1/', home1, name="home1"),
    path('admin/', admin.site.urls, name='admin'),
    
    # path('', include('oauth.urls')),
    
    path('dashbord/', generate_rewrite, name="dashbord"),
    path('dashboardRESum/', generate_summary, name="dashboardRESum"),
    path('dashboardRall/', extend_content, name="dashboardRall"),
    path('dashboardGEn/', chat_completion, name="dashboardGEn"),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              