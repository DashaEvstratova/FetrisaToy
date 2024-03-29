# FetrisaToy

<div id="header" align="center">
  <img src="https://sun9-61.userapi.com/impg/M48gAWjxxB46uLLmlQ34mx-OTSmbp4ylXRqKiQ/6ZG9W3Fr69U.jpg?size=1280x1280&quality=95&sign=e5f325281971a78c2031e054e156690a&type=albumf" width="200"/ >
</div>

## О проекте
Данный проект представляет собой интернет-магазин по продаже изделий из фетра ручной работы на стеке платформ Django и Vue.js. Также используется концепция REST API, поэтому для отдачи информации клиенту существует отдельный API. Вся информация о клиентах, товарах  и т.д. хранится в базе данных  PostgreSQL.


### Функционал покупателя:

- Возможность фильтровать товары.
- Возможность перехода на карточку товара, где есть выбор цвета и количество товара.
- Возможность оставлять отзыв на товар.
- Возможность добавлять в избранное понравившиеся товары.
- Возможность добавлять в корзину для заказа и далее совершить покупку.
- Покупатель также может получать скидки и применять промокоды.
- Оплата заказа.
- Результатом оплаты будут данные одного или нескольких товаров, все данные отсылаются на электронную почту покупателя, которую он указал при создании заказа.
- Покупатель может просмотреть свой профиль со всеми своими заказами.
- Возможность менять свои данные, а также сбрасывать пароль.

### Функционал администратора:

Для входа в админ-панель необходимо дописать в адресной строке `/admin`
, после Вы попадете на страницу авторизации где нужно ввести свои данные

- Возможность добавлять, удалять или редактировать товары на странице "Товары", так же можно посмотреть и информацию о товаре.
- Поиск товаров через поле поиска (нужно знать частичное или полное название товара).
- На главной странице есть небольшая статистика, где можно посмотреть: сумму проданных товаров, кол-во проданных товаров, кол-во товаров в наличии.

### Инструменты создания
<div>
<img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain.svg" title="Django" alt="Django" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/vuejs/vuejs-original.svg" title="Vue.js" alt="Vue.js" width="40" height="40"/>&nbsp;
</div>
