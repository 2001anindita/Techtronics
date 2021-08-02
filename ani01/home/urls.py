from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("shop",views.shop,name='shop'),
    path("contact",views.contact),
    path("checkout",views.user_login,name='checkout'),
    path("logout",views.logout,name='logout'),
    path("question",views.question_temp,name='ask your question'),
    path("answer/<int:id>",views.answer_temp,name='write your answers'),
    path("discuss/<int:id>",views.discuss_temp,name='discuss here'),
    path("lists",views.lists,name='search here'),
    path("dig",views.dig,name='digital electronics'),
    path("ana",views.ana,name='analog electronics'),
    path("micro",views.micro,name='microelectronics'),
    path("cir",views.cir,name='circuit design'),
    path("ic",views.ic,name='integrated circuits'),
    path("pow",views.pow,name='power electronics'),
    path("opto",views.opto,name='optoelectronics'),
    path("semi",views.semi,name='semiconductor devices'),
    path("emb",views.emb,name='embedded systems'),
    path("wire",views.wire,name='wireless communications'),
    path("nano",views.nano,name='nanoelectronics'),
    # path("sports",views.sports,name='sports'),
    path("ask",views.ask,name='ask'),
    path("ans",views.ans,name='ans'),
    # path("comment",views.comment,name='comment'),
    path("contact",views.contact,name='contact'),
    path('upload',views.upload,name='upload'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('edit/<int:id>',views.editstudentdetails),
    path('update/<int:id>',views.updatestudentdetails,name='updatestudentdetails'),
    path('delete/<int:id>',views.delstudent,name='delstudent'),
    path('upload_question',views.upload_question,name='upload_question'),
    path('upload_answer',views.upload_answer,name='upload_answer'),
    path('upload_comment',views.upload_comment,name='upload_comment'),
    # path("topic/<int:id>",views.view_topic)

    
    
]
