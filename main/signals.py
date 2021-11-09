from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Organization

# method for updating
@receiver(post_save, sender=Organization, dispatch_uid="send_email_upon_org_reg")
def send_email_upon_org_reg(sender, instance, created, **kwargs):
    if created and instance.rep_email:
        subject = "به پرسشنامه بررسی اثربخشی تیم‌های توسعه نرم‌افزار خوش آمدید."
        to = instance.rep_email
        html_message = render_to_string(
            "main/org_reg_success.html",
            {
                "org": instance.name,
                "rep_name": instance.rep_name,
                "token": instance.id.hashid,
            },
        )
        plain_message = strip_tags(html_message)
        send_mail(
            subject,
            plain_message,
            recipient_list=[to],
            html_message=html_message,
            from_email=None,
        )
    # mark as email sent
    # instance.email_sent = True
    # instance.save()
