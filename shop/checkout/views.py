from oscar.apps.checkout import views
from oscar.apps.payment import models

class PaymentDetailsView(views.PaymentDetailsView):
 
    print ("--------------------------ggdodo")   
    def handle_payment(self, order_number, total, **kwargs):
	print ("--------------------------ggdodo")
	reference = gateway.pre_auth(order_number, total.incl_tax, kwargs['bankcard'])
	
	source_type, __ = models.SourceType.objects.get_or_create(name="Stripe")
	source = models.Source(source_type= source_type, ammount_allocated=total.incl_tax, reference=reference)
	self.add_payment_source(source)
	
	self.add_payment_event('pre-auth', total.incl_tax) 
