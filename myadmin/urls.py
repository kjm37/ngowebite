from django.urls import path,include
from .import views
urlpatterns = [
    #for gallary curd



    path('',views.admingallaryx,name='admingallary'),
    path('addimage',views.add_image,name='addimage'),
    path('gal/<int:id>',views.del_galary,name='delete_gal'),
    path('updat/<int:id>',views.updat,name='updat'),

    path('vgalla',views.vadmingallaryx,name='vadmingallary'),
    path('vaddimage',views.vadd_image,name='vaddimage'),
    path('vgal/<int:id>',views.vdel_galary,name='vdelete_gal'),
    path('vupdat/<int:id>',views.vupdat,name='vupdat'),




    path('hgalla',views.hadmingallaryx,name='hadmingallary'),
    path('haddimage',views.hadd_image,name='haddimage'),
    path('hgal/<int:id>',views.hdel_galary,name='hdelete_gal'),
    path('hupdat/<int:id>',views.hupdat,name='hupdat'),



    path('agalla',views.aadmingallaryx,name='aadmingallary'),
    path('aaddimage',views.aadd_image,name='aaddimage'),
    path('agal/<int:id>',views.adel_galary,name='adelete_gal'),
    path('aupdat/<int:id>',views.aupdat,name='aupdat'),


    path('dgalla',views.dadmingallaryx,name='dadmingallary'),
    path('daddimage',views.dadd_image,name='daddimage'),
    path('dgal/<int:id>',views.ddel_galary,name='ddelete_gal'),
    path('dupdat/<int:id>',views.dupdat,name='dupdat'),


    path('cgalla',views.cadmingallaryx,name='cadmingallary'),
    path('caddimage',views.cadd_image,name='caddimage'),
    path('cgal/<int:id>',views.cdel_galary,name='cdelete_gal'),
    path('cupdat/<int:id>',views.cupdat,name='cupdat'),



    path('egalla',views.eadmingallaryx,name='eadmingallary'),
    path('eaddimage',views.eadd_image,name='eaddimage'),
    path('egal/<int:id>',views.edel_galary,name='edelete_gal'),
    path('eupdat/<int:id>',views.eupdat,name='eupdat'),


    path('ggalla',views.gadmingallaryx,name='gadmingallary'),
    path('gaddimage',views.gadd_image,name='gaddimage'),
    path('ggal/<int:id>',views.gdel_galary,name='gdelete_gal'),
    path('gupdat/<int:id>',views.gupdat,name='gupdat'),


    path('ugalla',views.uadmingallaryx,name='uadmingallary'),
    path('uaddimage',views.uadd_image,name='uaddimage'),
    path('ugal/<int:id>',views.udel_galary,name='udelete_gal'),
    path('uupdat/<int:id>',views.uupdat,name='uupdat'),


    path('cfgalla',views.cfadmingallaryx,name='cfadmingallary'),
    path('cfaddimage',views.cfadd_image,name='cfaddimage'),
    path('cfgal/<int:id>',views.cfdel_galary,name='cfdelete_gal'),
    path('cfupdat/<int:id>',views.cfupdat,name='cfupdat'),


    path('cigalla',views.ciadmingallaryx,name='ciadmingallary'),
    path('ciaddimage',views.ciadd_image,name='ciaddimage'),
    path('cigal/<int:id>',views.cidel_galary,name='cidelete_gal'),
    path('ciupdat/<int:id>',views.ciupdat,name='ciupdat'),



    path('ccfgalla',views.ccfadmingallaryx,name='ccfadmingallary'),
    path('ccfaddimage',views.ccfadd_image,name='ccfaddimage'),
    path('ccfgal/<int:id>',views.ccfdel_galary,name='ccfdelete_gal'),
    path('ccfupdat/<int:id>',views.ccfupdat,name='ccfupdat'),


    #for tile description curd
    path('titledisplay',views.title,name='title'),#display + add
    path('hd',views.hd,name='hd'),#input add
    path('h/<int:id>',views.hde,name='hde'),#delete
    path('titupdat/<int:id>',views.titleupdat,name='titupdat'),#update


        #for tile description curd
    path('titledisplay2',views.title2,name='title2'),#display + add
    path('hd2',views.hd2,name='hd2'),#input add
    path('h2/<int:id>',views.hde2,name='hde2'),#delete
    path('titupdat2/<int:id>',views.titleupdat2,name='titupdat2'),#update



    path('our',views.our,name='our'),#display + add
    path('ourdel/<int:id>',views.ourdel,name='ourdel'),
    path('addcause',views.addcause,name='addcause'),
    path('upo/<int:id>',views.upour,name='upou'),




    path('ent',views.displayevent,name='ent'),
    path('addevent',views.addevents,name='addevent'),
    path('eventdel/<int:id>',views.eventdel,name='eventdel'),
    path('upevent/<int:id>',views.upevent,name='upevent'),

    path('disteam',views.displayteam,name='disteam'),
    path('addteam',views.addteam,name='addteam'),
    path('teamdel/<int:id>',views.teamdel,name='teamdel'),
    path('upteam/<int:id>',views.upteam,name='upteam'),


    path('donateteam',views.donateteamm,name='donateteam'),
    path('dondel/<int:id>',views.dondel,name='dondel'),
    path('adddteam',views.adddteam,name='adddteam'),
    path('donupteam/<int:id>',views.donupteam,name='donupteam'),









]
