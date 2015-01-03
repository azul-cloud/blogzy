import datetime

from django.conf import settings
from django.core.mail import send_mail
from django.template import Context
from django.template.loader import get_template
from django.utils import timezone

from django_cron import CronJobBase, Schedule

from .models import PersonalBlog, Post, BlogSubscription, BlogSubscriptionLog


class NewsletterJob(CronJobBase):
    RUN_EVERY_MINS = None
    blogs = PersonalBlog.objects.all()
    days_ago = 0
    frequency = ""

    def do(self):
        '''
        We're going to go and get the emails that need to be sent.
        When we have the emails that need to be sent, we send the mass
        mail. 
        '''

        for b in self.blogs:
            '''
            if there are no subscribers to the blog, don't do anything. Also if there
            are no posts to be sent, don't do anything.
            '''
            if self.get_subscribers(b) and self.get_posts(b):
                newsletter = get_template('blogemail/newsletter.html').render(Context({
                    'posts': self.get_posts(b),
                    'blog': b,
                    'logo_url': settings.WEB_ROOT_URL + '/static/img/logo_dark.png'
                }))
            
                # send an individual email to each of the subscribers
                for s in self.get_subscribers(b):
                    send_mail(
                        'New posts from %s' % b,
                        '', # use html_message
                        'noreply@travelblogwave.com', 
                        [s],
                        html_message=newsletter
                    )

                    # log that the email was sent
                    subscription = BlogSubscription.objects.get(blog=b, email=s)
                    BlogSubscriptionLog.objects.create(subscription=subscription)


    def get_posts(self, blog):
        # get all the posts that should be included in the email
        posts = Post.objects.filter(active=True, blog=blog,
            create_date__gte=timezone.now().today() - datetime.timedelta(days=self.days_ago))
        return posts

    def get_subscribers(self, blog):
        # get a list of the subscriber emails
        email_list = blog.get_subscriber_emails(self.frequency)
        return email_list


class SendWeeklyNewsletters(NewsletterJob):
    RUN_EVERY_MINS = 5  #1 week
    days_ago = 20
    code = 'send_weekly_newsletters'
    frequency = "W"
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)


class SendMonthlyNewsletters(NewsletterJob):
    RUN_EVERY_MINS = 15  #1 month... just about
    days_ago = 31
    code = 'send_monthly_newsletters'
    frequency = "M"
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)



