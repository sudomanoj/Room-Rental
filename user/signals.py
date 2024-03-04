from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .models import Booking, House, Room

@receiver(post_save, sender=Booking)
def send_booking_notification(sender, instance, created, **kwargs):
    if created and instance.booked:
        if instance.house:  # Check if the booking is for a house
            # Send email to house landlord
            subject = "House booked notification"
            landlord_email = instance.house.user_email.email
        elif instance.room:  # Check if the booking is for a room
            # Send email to room landlord
            subject = "Room booked notification"
            landlord_email = instance.room.user_email.email
        else:
            return  # If neither house nor room is booked, do nothing

        # Construct email content
        context = {'booking': instance}
        html_message = render_to_string('email_template.html', context)
        plain_message = strip_tags(html_message)
        # Send email
        send_mail(
            subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            [landlord_email],
            html_message=html_message,
        )
        
        
@receiver(post_delete, sender=Booking)
def update_house_booking_status(sender, instance, **kwargs):
    house = instance.house
    if house:
        house.booked = False
        house.save()
        
@receiver(post_delete, sender=Booking)
def update_room_booking_status(sender, instance, **kwargs):
    room = instance.room
    if room:
        room.booked = False
        room.save()
        
# @receiver(pre_save, sender=Room)
# def delete_booking_on_room_marking(sender, instance, **kwargs):
#     # Check if the booking is being marked as false
#     if instance.booked == False:
#         # Check if the room has an associated booking
#         if hasattr(instance, 'booking'):
#             # Delete the associated booking
#             instance.booking.delete()
#             instance.save()


@receiver(post_save, sender=Room)
def delete_booking_on_room_marking(sender, instance, created, **kwargs):
    # Check if the room is being marked as unbooked and it's not a newly created room
    if not instance.booked and not created:
        # Check if the room has an associated booking
        try:
            booking = Booking.objects.get(room_id=instance)
            # Delete the associated booking
            booking.delete()
        except Booking.DoesNotExist:
            pass  # No associated booking found, do nothing

            
@receiver(pre_save, sender=House)
def delete_booking_on_house_marking(sender, instance, **kwargs):
    # Check if the booking is being marked as false
    if instance.booked == False:
        # Check if the room has an associated booking
        if hasattr(instance, 'booking'):
            # Delete the associated booking
            instance.booking.delete()
            instance.save()