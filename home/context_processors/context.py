from home.forms import SubscribeMailingForm


def mailing_form(request):
    return {"email_form": SubscribeMailingForm()}
