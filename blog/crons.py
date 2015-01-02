from django.core.mail import send_mail

from django_cron import CronJobBase, Schedule


class SendNewsletters(CronJobBase):
    RUN_EVERY_MINS = 2

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'send_newsletters'    # a unique code

    def do(self):
        '''
        We're going to go and get the emails that need to be sent.
        When we have the emails that need to be sent, we send the mass
        mail. 
        '''
        send_mail(
            'From Cron!', 
            'This email has been sent from a cron job.',
            'travelblogwave@gmail.com', 
            ['awwester@gmail.com']
        )