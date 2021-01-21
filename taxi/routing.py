from django.core.asgi import get_asgi_application
from django.urls import path # new
from channels.routing import ProtocolTypeRouter, URLRouter # changed
from trips.consumers import TaxiConsumer
from taxi.middleware import TokenAuthMiddlewareStack # new

application = ProtocolTypeRouter({
    'http': get_asgi_application(),

    'websocket': TokenAuthMiddlewareStack(
        URLRouter([
            path('taxi/', TaxiConsumer.as_asgi()),
        ])
    ),
})