class Constants:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'

    COURIER_URL = f'{BASE_URL}/api/v1/courier'
    LOGIN_COURIER_URL = f'{BASE_URL}/api/v1/courier/login'
    DELETE_COURIER_URL = f'{BASE_URL}/api/v1/courier/{{}}'

    ORDER_URL = f'{BASE_URL}/api/v1/orders/'
    ACCEPT_ORDER_URL = f'{BASE_URL}/api/v1/orders/accept/{{}}?courierId={{}}'
    ACCEPT_ORDER_URL_NON_COURIER_ID = f'{BASE_URL}/api/v1/orders/accept/{{}}'
    ACCEPT_ORDER_URL_NON_ORDER_ID = f'{BASE_URL}/api/v1/orders/accept/?courierId={{}}'
    FIND_ORDER_URL = f'{BASE_URL}/api/v1/orders/track?t={{}}'
    FIND_ORDER_URL_NON_TRACK = f'{BASE_URL}/api/v1/orders/track'
    CANCEL_ORDER_URL = f'{BASE_URL}/api/v1/orders/cancel?track={{}}'
