from django.shortcuts import render,redirect,get_object_or_404
from .models import*
from django.contrib.auth import authenticate
from django.contrib import messages
from django.utils import timezone
from datetime import date
from django.db.models import Q

# Create your views here.

def index(request):

    return render(request,"index.html")

def login(request):

    if request.POST:
        email=request.POST['email']
        password=request.POST['password']

        user=authenticate(username=email,password=password)

        if user:
            if user.is_active:
                if user.is_superuser:
                    return redirect('/admin_home')
                elif user.usertype=="farmer":
                    user = Farmer_registration.objects.get(email=email)
                    if user.admin_approval:
                        request.session["email"] = email
                        request.session["id"] = user.id
                        return redirect('/farmer_home')
                    else:
                        messages.info(request,"Your account is not yet approved by an admin")
                        redirect('/login')

                elif user.usertype=="supplier":
                    user = Supplier_registration.objects.get(email=email)
                    if user.admin_approval:
                        request.session["email"] = email
                        request.session["id"] = user.id
                        return redirect('/supplier_home')
                    else:
                        messages.info(request,"Your account is not yet approved by an admin")
                        redirect('/login')

                elif user.usertype=="specialist":
                    user = Specialist_registration.objects.get(email=email)
                    if user.admin_approval:
                        request.session["email"] = email
                        request.session["id"] = user.id
                        return redirect('/specialist_home')
                    else:
                        messages.info(request,"Your account is not yet approved by an admin")
                        redirect('/login')
           

    return render(request,"login.html")

def registration_farmer(request):

    if request.POST:
        name=request.POST['name']
        contact=request.POST['contact']
        address=request.POST['address']
        email=request.POST['email']
        password=request.POST['password']
        id_proof=request.FILES['id_proof']
        profile_picture=request.FILES['profile_picture']

        log=Login_table.objects.create_user(username=email,password=password,usertype='farmer')
        log.save()

        farmer=Farmer_registration.objects.create(
            name=name,
            contact=contact,
            address=address,
            email=email,
            id_proof=id_proof,
            profile_picture=profile_picture,
            login_id=log
        )
        farmer.save()
        messages.info(request,"Registration successful,Wait for admin approvel")

    return render(request,"registration_farmer.html")

def registration_supplier(request):

    if request.POST:
        name=request.POST['name']
        contact=request.POST['contact']
        address=request.POST['address']
        email=request.POST['email']
        password=request.POST['password']
        id_proof=request.FILES['id_proof']
        licence=request.FILES['licence']
        profile_picture=request.FILES['profile_picture']

        log=Login_table.objects.create_user(username=email,password=password,usertype='supplier')
        log.save()

        supplier=Supplier_registration.objects.create(
            name=name,
            contact=contact,
            address=address,
            email=email,
            id_proof=id_proof,
            licence=licence,
            profile_picture=profile_picture,
            login_id=log
        )
        supplier.save()
        messages.info(request,"Registration successful,Wait for admin approvel")


    return render(request,"registration_supplier.html")

def registration_specialist(request):

    if request.POST:
        name=request.POST['name']
        contact=request.POST['contact']
        address=request.POST['address']
        email=request.POST['email']
        password=request.POST['password']
        id_proof=request.FILES['id_proof']
        licence=request.FILES['licence']
        profile_picture=request.FILES['profile_picture']

        log=Login_table.objects.create_user(username=email,password=password,usertype='specialist')
        log.save()

        specialist=Specialist_registration.objects.create(
            name=name,
            contact=contact,
            address=address,
            email=email,
            id_proof=id_proof,
            licence=licence,
            profile_picture=profile_picture,
            login_id=log
        )
        specialist.save()
        messages.info(request,"Registration successful,Wait for admin approvel")


    return render(request,"registration_specialist.html")



#################### ADMIN ###########################

def admin_home(request):

    farmer_count=0
    supplier_count=0
    specialist_count=0

    farmer=Farmer_registration.objects.filter(admin_approval=True)
    supplier=Supplier_registration.objects.filter(admin_approval=True)
    specialist=Specialist_registration.objects.filter(admin_approval=True)
   
    for f in farmer:
        farmer_count+=1
        f.id
    for s in supplier:
        supplier_count+=1
        s.id
    for i in specialist:
        specialist_count+=1
        i.id

    return render(request,"admin/admin_home.html",
    {
       "farmer_count":farmer_count,
       "supplier_count":supplier_count,
       "specialist_count":specialist_count,
    })


def admin_view_farmer_requests(request):

    farmers=Farmer_registration.objects.filter(admin_approval=False)

    return render(request,"admin/view_farmer_request.html",{"farmers":farmers})

def admin_view_farmer_request_single(request):

    did=request.GET.get('id')
    farmer=Farmer_registration.objects.get(id=did)

    return render(request,"admin/view_farmer_request_single.html",{"farmer":farmer})


def admin_accept_farmer_request(request):

    did=request.GET.get('id')
    farmer=Farmer_registration.objects.get(id=did)
    farmer.admin_approval=True
    farmer.save()
    messages.info(request,"Accepted Sucessfully")

    return redirect('/admin_view_farmer_requests')

def admin_reject_farmer_request(request):

    did=request.GET.get('id')
    farmer=Farmer_registration.objects.get(id=did)
    farmer.delete()
    log=Login_table.objects.get(username=farmer.login_id)
    log.delete()
    messages.info(request,"Rejected Sucessfully")

    return redirect('/admin_view_farmer_requests')

def admin_view_farmers(request):

    farmers=Farmer_registration.objects.filter(admin_approval=True)

    return render(request,"admin/admin_view_farmers.html",{"farmers":farmers})

def admin_view_farmer_single(request):

    did=request.GET.get('id')
    farmer=Farmer_registration.objects.get(id=did)

    return render(request,"admin/admin_view_farmer_single.html",{"farmer":farmer})

def admin_delete_farmer(request):

    did=request.GET.get('id')
    farmer=Farmer_registration.objects.get(id=did)
    farmer.delete()
    log=Login_table.objects.get(username=farmer.login_id)
    log.delete()
    messages.info(request,"Removed successfully")

    return redirect('/admin_view_farmers')


def admin_view_supplier_requests(request):

    suppliers=Supplier_registration.objects.filter(admin_approval=False)

    return render(request,"admin/view_supplier_request.html",{"suppliers":suppliers})

def admin_view_supplier_request_single(request):

    tid=request.GET.get('id')
    supplier=Supplier_registration.objects.get(id=tid)

    return render(request,"admin/view_supplier_request_single.html",{"supplier":supplier})

def admin_accept_supplier_request(request):

    tid=request.GET.get('id')
    supplier=Supplier_registration.objects.get(id=tid)
    supplier.admin_approval=True
    supplier.save()
    messages.info(request,"Accepted Sucessfully")

    return redirect('/admin_view_supplier_requests')

def admin_reject_supplier_request(request):

    tid=request.GET.get('id')
    supplier=Supplier_registration.objects.get(id=tid)
    supplier.delete()
    log=Login_table.objects.get(username=supplier.login_id)
    log.delete()
    messages.info(request,"Rejected Sucessfully")

    return redirect('/admin_view_supplier_requests')

def admin_view_suppliers(request):

    suppliers=Supplier_registration.objects.filter(admin_approval=True)

    return render(request,"admin/admin_view_suppliers.html",{"suppliers":suppliers})

def admin_view_supplier_single(request):

    tid=request.GET.get('id')
    supplier=Supplier_registration.objects.get(id=tid)

    return render(request,"admin/admin_view_supplier_single.html",{"supplier":supplier})

def admin_delete_supplier(request):

    tid=request.GET.get('id')
    supplier=Supplier_registration.objects.get(id=tid)
    supplier.delete()
    log=Login_table.objects.get(username=supplier.login_id)
    log.delete()
    messages.info(request,"Removed successfully")

    return redirect('/admin_view_suppliers')

def admin_view_specialist_requests(request):

    specialists=Specialist_registration.objects.filter(admin_approval=False)

    return render(request,"admin/view_specialist_request.html",{"specialists":specialists})

def admin_view_specialist_request_single(request):

    tid=request.GET.get('id')
    specialist=Specialist_registration.objects.get(id=tid)

    return render(request,"admin/view_specialist_request_single.html",{"specialist":specialist})

def admin_accept_specialist_request(request):

    tid=request.GET.get('id')
    specialist=Specialist_registration.objects.get(id=tid)
    specialist.admin_approval=True
    specialist.save()
    messages.info(request,"Accepted Sucessfully")

    return redirect('/admin_view_specialist_requests')

def admin_reject_specialist_request(request):

    tid=request.GET.get('id')
    specialist=Specialist_registration.objects.get(id=tid)
    specialist.delete()
    log=Login_table.objects.get(username=specialist.login_id)
    log.delete()
    messages.info(request,"Rejected Sucessfully")

    return redirect('/admin_view_specialist_requests')


def admin_view_specialists(request):

    specialists=Specialist_registration.objects.filter(admin_approval=True)

    return render(request,"admin/admin_view_specialists.html",{"specialists":specialists})

def admin_view_specialist_single(request):

    tid=request.GET.get('id')
    specialist=Specialist_registration.objects.get(id=tid)

    return render(request,"admin/admin_view_specialist_single.html",{"specialist":specialist})

def admin_delete_specialist(request):

    tid=request.GET.get('id')
    specialist=Specialist_registration.objects.get(id=tid)
    specialist.delete()
    log=Login_table.objects.get(username=specialist.login_id)
    log.delete()
    messages.info(request,"Removed successfully")

    return redirect('/admin_view_specialists')

def admin_add_tutorial(request):

    if request.POST:
        title=request.POST['title']
        description=request.POST['description']
        video_link=request.POST['video_link']

        tutorial=Add_tutorials.objects.create(
            title=title,
            description=description,
            video_link=video_link,
            posted_on=timezone.now()
        )
        tutorial.save()
        messages.info(request,"Posted successfully")
        return redirect('/admin_view_tutorials')

    return render(request,"admin/admin_add_tutorial.html")

def admin_update_tutorial(request):

    tid=request.GET.get('id')
    tutorial=Add_tutorials.objects.get(id=tid)

    if request.POST:
        title=request.POST['title']
        tutorial.title=title
        description=request.POST['description']
        tutorial.description=description
        video_link=request.POST['video_link']
        tutorial.video_link=video_link
        tutorial.save()
        messages.info(request,"Updated successfully")
        return redirect('/admin_view_tutorials')

    return render(request,"admin/admin_update_tutorial.html",{"tutorial":tutorial})

def admin_delete_tutorial(request):

    tid=request.GET.get('id')
    tutorial=Add_tutorials.objects.get(id=tid)
    tutorial.delete()

    messages.info(request,"Deleted successfully")
    return redirect('/admin_view_tutorials')

def admin_view_tutorials(request):

    tutorials=Add_tutorials.objects.all()

    return render(request,"admin/admin_view_tutorials.html",{"tutorials":tutorials})

def admin_view_tutorial_single(request):

    tid=request.GET.get('id')
    tutorial=Add_tutorials.objects.get(id=tid)

    return render(request,"admin/admin_view_tutorial_single.html",{"tutorial":tutorial})

def admin_add_category(request):

    if request.POST:
        category=request.POST['category']
        category_image=request.FILES['category_image']

        categories=Add_categories.objects.create(
            category=category,
            category_image=category_image
        )
        categories.save()
        messages.info(request,"Added successfully")
        return redirect('/admin_view_categories')

    return render(request,"admin/admin_add_category.html")

def admin_view_categories(request):

    categories=Add_categories.objects.all()

    return render(request,"admin/admin_view_categories.html",{"categories":categories})

def admin_update_category(request):

    cid=request.GET.get('id')
    categories=Add_categories.objects.get(id=cid)

    if request.POST:
        category=request.POST['category']
        categories.category=category
        category_image=request.FILES['category_image']
        categories.category_image=category_image

        categories.save()
        messages.info(request,"Updated successfully")
        return redirect('/admin_view_categories')

    return render(request,"admin/admin_update_category.html",{"category":categories})

def admin_delete_category(request):

    cid=request.GET.get('id')
    categories=Add_categories.objects.get(id=cid)
    categories.delete()
    messages.info(request,"Deleted successfully")
    return redirect('/admin_view_categories')

def admin_view_feedbacks(request):

    feedbacks=Feedback.objects.all()

    return render(request,"admin/admin_view_feedbacks.html",{"feedbacks":feedbacks})

def admin_view_bookings(request):

    bookings=Booking.objects.all()

    return render(request,"admin/admin_view_bookings.html",{"bookings":bookings})


#################### FARMER ###########################
 
def farmer_home(request):

    id=request.session['id']
    farmer=Farmer_registration.objects.get(id=id)

    return render(request,"farmer/farmer_home.html",{"farmer":farmer})

def farmer_view_tutorials(request):

    tutorials=Add_tutorials.objects.all()

    return render(request,"farmer/farmer_view_tutorials.html",{"tutorials":tutorials})

def farmer_searched_tutorial(request):

    if request.POST:
        searched=request.POST['searched']
        tutorials=Add_tutorials.objects.filter(Q(title__icontains=searched))

        return render(request,"farmer/farmer_searched_tutorial.html",{"searched":searched,"tutorials":tutorials})
    else:
        return render(request,"farmer/farmer_searched_tutorial.html")

def farmer_view_products(request):

    products=Add_products.objects.all()

    return render(request,"farmer/farmer_view_products.html",{"products":products})

def farmer_view_product_single(request):

    pid=request.GET.get('id')
    product=Add_products.objects.get(id=pid)

    return render(request,"farmer/farmer_view_product_single.html",{"product":product})

def farmer_booking_product(request):

    id=request.session['id']
    farmer_id=Farmer_registration.objects.get(id=id)

    total_price=0 
    
    if request.POST:
        quantity=request.POST['quantity']
        shipping_address=request.POST['shipping_address']
        product_id=request.POST['product_id']

        product_obj=Add_products.objects.get(id=product_id)


        current_price=product_obj.price
        total_price=int(current_price)*int(quantity) 

        current_quantity=int(product_obj.quantity) - int(quantity)

        product_obj.quantity=current_quantity
        product_obj.save()



        booking=Booking.objects.create(
            quantity=quantity,
            farmer_id=farmer_id,
            shipping_address=shipping_address,
            product_id=product_obj,
            booking_status=True,
            total_price=total_price,
            booked_on=timezone.now()
        )
        booking.save()
    return redirect(f'/farmer_payment?id={booking.id}')

def farmer_payment(request):

    bid=request.GET.get('id')
    booking=Booking.objects.get(id=bid)
    
    if request.POST:
        booking.payment_status=True
        booking.save()

        messages.info(request,"Booking confirmed")

        return redirect('/farmer_view_bookings')

    return render(request,"farmer/farmer_payment.html",{"booking":booking})

def farmer_view_bookings(request):

    id=request.session['id']
    farmer_id=Farmer_registration.objects.get(id=id)
    bookings=Booking.objects.filter(farmer_id=farmer_id)

    return render(request,"farmer/farmer_view_bookings.html",{"bookings":bookings})

def farmer_cancel_booking(request):

    bid=request.GET.get('id')
    booking=Booking.objects.get(id=bid)
    booking.cancel_status=True
    booking.save()
    pid=booking.product_id
    booking_quantity=booking.product_id.quantity
    product=Add_products.objects.get(id=pid.id)
    product.quantity=int(product.quantity) + int(booking.quantity)
    product.save()
    messages.info(request,"Booking Cancelled")

    return redirect('/farmer_view_bookings')

def farmer_view_specialists(request):

    specialists=Specialist_registration.objects.filter(admin_approval=True)

    return render(request,"farmer/farmer_view_specialists.html",{"specialists":specialists})

def farmer_message_specialists(request):

    sid=request.GET.get('id')
    specialist=Specialist_registration.objects.get(id=sid)
    fid=request.session['id']
    farmer=Farmer_registration.objects.get(id=fid)

    if request.POST:
        message=request.POST['message']

        chat=Farmer_specialist_chat.objects.create(
            message=message,
            specialist_id=specialist,
            farmer_id=farmer,
            message_on=timezone.now()
        )
        chat.save()
        messages.info(request,"Message send successfully")
        return redirect('/farmer_view_messages')

    return render(request,"farmer/farmer_chat_with_specialists.html",{"specialist":specialist})

def farmer_view_messages(request):

    id=request.session['id']
    farmer_id=Farmer_registration.objects.get(id=id)

    chats=Farmer_specialist_chat.objects.filter(farmer_id=farmer_id)

    return render(request,"farmer/farmer_view_messages.html",{"chats":chats})

def farmer_add_feedback(request):

    id=request.session['id']
    farmer_id=Farmer_registration.objects.get(id=id)

    if request.POST:
        feedback=request.POST['feedback']
        rating=request.POST['rating']

        feed=Feedback.objects.create(
            feedback=feedback,
            rating=rating,
            farmer_id=farmer_id,
            user_type="farmer",
            feedback_on=timezone.now()
        )
        feed.save()
        messages.info(request,"Feedback Sent successfully")
        return redirect('/farmer_view_feedbacks')

    return render(request,"farmer/farmer_add_feedback.html")

def farmer_view_feedbacks(request):

    feedbacks=Feedback.objects.all()

    return render(request,"farmer/farmer_view_feedbacks.html",{"feedbacks":feedbacks})

#################### SUPPLIER ###########################

def supplier_home(request):
    id=request.session['id']
    supplier=Supplier_registration.objects.get(id=id)

    return render(request,"supplier/supplier_home.html",{"supplier":supplier})

def supplier_add_product(request):

    id=request.session['id']
    supplier_id=Supplier_registration.objects.get(id=id)

    categories=Add_categories.objects.all()

    if request.POST:
        product=request.POST['product']
        category_id=request.POST['category_id']
        description=request.POST['description']
        product_image=request.FILES['product_image']
        quantity=request.POST['quantity']
        price=request.POST['price']

        category_id=Add_categories.objects.get(id=category_id)

        product=Add_products.objects.create(
            product=product,
            category_id=category_id,
            description=description,
            product_image=product_image,
            quantity=quantity,
            price=price,
            supplier_id=supplier_id,

        )
        product.save()
        messages.info(request,"Product Added Successfully")

    return render(request,"supplier/supplier_add_product.html",{"categories":categories})

def supplier_view_products(request):

    id=request.session['id']
    products=Add_products.objects.filter(supplier_id=id)
    return render(request,"supplier/supplier_view_products.html",{"products":products})

def supplier_view_product_single(request):

    pid=request.GET.get('id')
    product=Add_products.objects.get(id=pid)

    return render(request,"supplier/supplier_view_product_single.html",{"product":product})

def supplier_add_feedback(request):

    id=request.session['id']
    supplier_id=Supplier_registration.objects.get(id=id)

    if request.POST:
        feedback=request.POST['feedback']
        rating=request.POST['rating']

        feed=Feedback.objects.create(
            feedback=feedback,
            rating=rating,
            supplier_id=supplier_id,
            user_type="supplier",
            feedback_on=timezone.now()
        )
        feed.save()
        messages.info(request,"Feedback Sent successfully")
        return redirect('/supplier_view_feedbacks')

    return render(request,"supplier/supplier_add_feedback.html")

def supplier_update_product(request):

    pid=request.GET.get('id')
    product_obj=Add_products.objects.get(id=pid)
    categories=Add_categories.objects.all()

    if request.POST:
        product=request.POST['product']
        product_obj.product=product
        category_id=request.POST['category_id']
        category_id=Add_categories.objects.get(id=category_id)
        product_obj.category_id=category_id
        description=request.POST['description']
        product_obj.description=description
        quantity=request.POST['quantity']
        product_obj.quantity=quantity
        price=request.POST['price']
        product_obj.price=price
        product_image=request.FILES['product_image']
        product_obj.product_image=product_image

        product_obj.save()
        messages.info(request,"Updated Successfully")
        return redirect('/supplier_view_products')

    return render(request,"supplier/supplier_update_product.html",{
        "product":product_obj,
        "categories":categories})

def supplier_delete_product(request):

    pid=request.GET.get('id')
    product=Add_products.objects.get(id=pid)
    product.delete()
    messages.info(request,"Updated Successfully")
    return redirect('/supplier_view_products')

def supplier_view_feedbacks(request):

    feedbacks=Feedback.objects.all()

    return render(request,"supplier/supplier_view_feedbacks.html",{"feedbacks":feedbacks})

def supplier_view_bookings(request):

    bookings=Booking.objects.all()

    return render(request,"supplier/supplier_view_bookings.html",{"bookings":bookings})



#################### SPECIALIST ###########################

def specialist_home(request):
    id=request.session['id']
    specialist=Specialist_registration.objects.get(id=id)

    return render(request,"specialist/specialist_home.html",{"specialist":specialist})

def specialist_view_messages(request):

    id=request.session['id']
    specialist_id=Specialist_registration.objects.get(id=id)
    chats=Farmer_specialist_chat.objects.filter(specialist_id=specialist_id)

    return render(request,"specialist/specialist_view_messages.html",{"chats":chats})

def specialist_reply_farmer(request):

    cid=request.GET.get('id')
    chat=Farmer_specialist_chat.objects.get(id=cid)

    if request.POST:
        reply=request.POST['reply']
        chat.reply=reply
        chat.reply_on=timezone.now()
        chat.save()

        messages.info(request,"Replay sent successfully")

        return redirect('/specialist_view_messages')
    return render(request,"specialist/specialist_reply_farmer.html",{"chat":chat})
   
def specialist_add_feedback(request):

    id=request.session['id']
    specialist_id=Specialist_registration.objects.get(id=id)

    if request.POST:
        feedback=request.POST['feedback']
        rating=request.POST['rating']

        feed=Feedback.objects.create(
            feedback=feedback,
            rating=rating,
            specialist_id=specialist_id,
            user_type="specialist",
            feedback_on=timezone.now()
        )
        feed.save()
        messages.info(request,"Feedback Sent successfully")
        return redirect('/specialist_view_feedbacks')

    return render(request,"specialist/specialist_add_feedback.html")

def specialist_view_feedbacks(request):

    feedbacks=Feedback.objects.all()

    return render(request,"specialist/specialist_view_feedbacks.html",{"feedbacks":feedbacks})


