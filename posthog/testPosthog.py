import posthog
from dateutil.tz import tzutc
from datetime import datetime

# Substitutes posthog.api_key which still exists but has been deprecated
posthog.project_api_key = 'phc_VDgFtMEcVDE9FweJZR0s9LtqfNvyawHLPWDDLtXN1Y1'

# Only necessary if you want to use feature flags
posthog.personal_api_key = 'phx_BN2GhQiu2Rc3JICy60OR6uCv2zDnxiOFrAWV46cZisu'

# You can remove this line if you're using app.posthog.com
posthog.host = 'http://127.0.0.1:8000'

posthog.debug = True

posthog.identify('1', {
    'email': 'nfrank@gmail.com',
    'name': 'Nick Frank',
    'customerSession': 'CustomerSession',
})
#posthog.capture('distinct id', 'movie played', {'movie_id': '123', 'category': 'romcom'})
#posthog.capture('distinct id', event='movie played', properties={'movie_id': '123', 'category': 'romcom'}, timestamp=datetime.utcnow().replace(tzinfo=tzutc()))

posthog.capture('1', '$pageview', {'$current_url': 'https://example.com'})

print("Hello world")