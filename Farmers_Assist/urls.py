
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('login',views.login),
    path('registration_farmer',views.registration_farmer),
    path('registration_supplier',views.registration_supplier),
    path('registration_specialist',views.registration_specialist),
   
   ################# Admin ####################
   
    path('admin_home',views.admin_home),
    path('admin_view_farmer_requests',views.admin_view_farmer_requests),
    path('admin_view_farmer_request_single',views.admin_view_farmer_request_single),
    path('admin_accept_farmer_request',views.admin_accept_farmer_request),
    path('admin_reject_farmer_request',views.admin_reject_farmer_request),
    path('admin_view_farmers',views.admin_view_farmers),
    path('admin_view_farmer_single',views.admin_view_farmer_single),
    path('admin_delete_farmer',views.admin_delete_farmer),
    path('admin_view_supplier_requests',views.admin_view_supplier_requests),
    path('admin_view_supplier_request_single',views.admin_view_supplier_request_single),
    path('admin_accept_supplier_request',views.admin_accept_supplier_request),
    path('admin_reject_supplier_request',views.admin_reject_supplier_request),
    path('admin_view_suppliers',views.admin_view_suppliers),
    path('admin_view_supplier_single',views.admin_view_supplier_single),
    path('admin_delete_supplier',views.admin_delete_supplier),
    path('admin_view_specialist_requests',views.admin_view_specialist_requests),
    path('admin_view_specialist_request_single',views.admin_view_specialist_request_single),
    path('admin_accept_specialist_request',views.admin_accept_specialist_request),
    path('admin_reject_specialist_request',views.admin_reject_specialist_request),
    path('admin_view_specialists',views.admin_view_specialists),
    path('admin_view_specialist_single',views.admin_view_specialist_single),
    path('admin_delete_specialist',views.admin_delete_specialist),
    path('admin_add_tutorial',views.admin_add_tutorial),
    path('admin_update_tutorial',views.admin_update_tutorial),
    path('admin_delete_tutorial',views.admin_delete_tutorial),
    path('admin_view_tutorials',views.admin_view_tutorials),
    path('admin_view_tutorial_single',views.admin_view_tutorial_single),
    path('admin_add_category',views.admin_add_category),
    path('admin_view_categories',views.admin_view_categories),
    path('admin_update_category',views.admin_update_category),
    path('admin_delete_category',views.admin_delete_category),
    path('admin_view_feedbacks',views.admin_view_feedbacks),
    path('admin_view_bookings',views.admin_view_bookings),

   ################# Farmer ###################
   
    path('farmer_home',views.farmer_home),
    path('farmer_view_tutorials',views.farmer_view_tutorials),
    path('farmer_view_products',views.farmer_view_products),
    path('farmer_view_product_single',views.farmer_view_product_single),
    path('farmer_booking_product',views.farmer_booking_product),
    path('farmer_payment',views.farmer_payment),
    path('farmer_view_bookings',views.farmer_view_bookings),
    path('farmer_cancel_booking',views.farmer_cancel_booking),
    path('farmer_view_specialists',views.farmer_view_specialists),
    path('farmer_message_specialists',views.farmer_message_specialists),
    path('farmer_view_messages',views.farmer_view_messages),
    path('farmer_add_feedback',views.farmer_add_feedback),
    path('farmer_view_feedbacks',views.farmer_view_feedbacks),
    path('farmer_searched_tutorial',views.farmer_searched_tutorial),


   ################# Supplier #################

    path('supplier_home',views.supplier_home),
    path('supplier_add_product',views.supplier_add_product),
    path('supplier_view_products',views.supplier_view_products),
    path('supplier_view_product_single',views.supplier_view_product_single),
    path('supplier_update_product',views.supplier_update_product),
    path('supplier_delete_product',views.supplier_delete_product),
    path('supplier_view_bookings',views.supplier_view_bookings),
    path('supplier_add_feedback',views.supplier_add_feedback),
    path('supplier_view_feedbacks',views.supplier_view_feedbacks),

    
   ################# Specialist ###############
   
    path('specialist_home',views.specialist_home),
    path('specialist_view_messages',views.specialist_view_messages),
    path('specialist_reply_farmer',views.specialist_reply_farmer),
    path('specialist_add_feedback',views.specialist_add_feedback),
    path('specialist_view_feedbacks',views.specialist_view_feedbacks),
   
]#
