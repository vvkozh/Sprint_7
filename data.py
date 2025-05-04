class OrderData:
    COLOR = ['', 'BLACK', 'GREY', ['BLACK', 'GREY']]

class Response:
    RESPONSE_CREATE_ORDER = 'track'
    RESPONSE_SUCCESS = {'ok': True}
    RESPONSE_DELETE_WITHOUT_ID = {'code': 400 ,'message': 'Недостаточно данных для удаления курьера.'}
    RESPONSE_DELETE_INVALID_ID = {'code': 404 ,'message': 'Курьера с таким id нет.'}
    RESPONSE_NOT_ID = {'code': 400 ,'message': 'Недостаточно данных для поиска'}
    RESPONSE_INVALID_ID = [
        {'code': 404 ,'message': 'Заказа с таким id не существует'},
        {'code': 404 ,'message': 'Курьера с таким id не существует'}
    ]
    RESPONSE_WITHOUT_TRACK = {'code': 400 ,'message': 'Недостаточно данных для поиска'}
    RESPONSE_INVALID_TRACK = {'code': 404, 'message': 'Заказ не найден'}
    RESPONSE_DUPLICATE_LOGIN = {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
    RESPONSE_FAILED_CREATE_COURIER = {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}