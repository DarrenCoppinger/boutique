from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        """
        everytime a line item is saved or deleted our custom
        update total model method will be called updating order 
        totals automatically

        """
        import checkout.signals
