from django.conf import settings


def main(request):
    google_api_key = settings.GOOGLE_API_KEY
    userreport_key = settings.USERREPORT_KEY
    offline = settings.OFFLINE

    return {
    	"google_api_key": google_api_key,
    	"userreport_key": userreport_key,
        "offline": offline,
    }