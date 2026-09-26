class TextErrorAcceptOrder:
    TEXT_RESPONSE_ACCEPR_ORDER_WITHOUT_ID = "Недостаточно данных для поиска"
    TEXT_RESPONSE_COURIER_NOT_FOUND = "Курьера с таким id не существует"
    TEXT_RESPONSE_ORDER_NOT_FOUND = "Заказа с таким id не существует"
    TEXT_RESPONSE_DATA_NOT_FOUND = "Not Found."

class TextErrorCreateCourier:
    TEXT_RESPONSE_USED_LOGIN = "Этот логин уже используется. Попробуйте другой."
    TEXT_RESPONSE_NOT_ENOUGH_DATA = "Недостаточно данных для создания учетной записи"

class TextErrorDeleteCourier:
    TEXT_RESPONSE_NOT_ENOUGH_ID = "Not Found."
    TEXT_RESPONSE_COURIER_NOT_FOUND = "Курьера с таким id нет."

class TextErrorFoundByNumber:
    TEXT_RESPONSE_NOT_ENOUGH_DATA = "Недостаточно данных для поиска"
    TEXT_RESPONSE_ORDER_NOT_FOUND = "Заказ не найден"

class TextErrorLoginCourier:
    TEXT_RESPONSE_NOT_ENOUGH_DATA = "Недостаточно данных для входа"
    TEXT_RESPONSE_COURIER_NOT_FOUND = "Учетная запись не найдена"
    TEXT_RESPONSE_SERVICE_UNVAILABLE = 'Service unavailable'