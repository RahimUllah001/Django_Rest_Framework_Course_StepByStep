from rest_framework.throttling import UserRateThrottle


class CustomThrotleRate(UserRateThrottle):
    scope = 'custom'