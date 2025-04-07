from celery import shared_task
from .models import Loan
from django.core.mail import send_mail
from django.conf import settings
from datetime import date, datetime, timedelta


@shared_task
def send_loan_notification(loan_id):
    try:
        loan = Loan.objects.get(id=loan_id)
        member_email = loan.member.user.email
        book_title = loan.book.title
        send_mail(
            subject='Book Loaned Successfully',
            message=f'Hello {loan.member.user.username},\n\nYou have successfully loaned "{book_title}".\nPlease return it by the due date.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[member_email],
            fail_silently=False,
        )
    except Loan.DoesNotExist:
        pass

@shared_task
def check_overdue_loans():
    try:
        loans = Loan.objects.filter(is_returned=False).filter(due_date < date.today)
        for x in loans:
            member_email = x.member.user.email
            print(f"sending email to {x.member}")
            book_title = x.book.title
            send_mail(
                subject='Book Loaned Successfully',
                message=f'Hello {x.member.user.username},\n\n Just to remind you have overdue books.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[member_email],
                fail_silently=False,
            )
    except:
        pass