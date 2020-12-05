# import re
#
# from django.http import JsonResponse
# from django.utils import translation
# from django.utils.deprecation import MiddlewareMixin
# from django.utils.translation import ugettext as _
# from rest_framework import status
# from rest_framework.views import APIView
# from time import time, sleep
#
# from .views import BaseView
#
#
# class PersonalPageMiddleware(MiddlewareMixin, BaseView, APIView):
#     request_time = 0
#
#     def process_view(self, request, view_func, view_args, view_kwargs):
#         self.request_time = time()
#
#         # Default context
#         # redirect: ссылка после котороый будет производится редирект на нужную страицу
#         # redirect_by_button: используется вместе с "message" когда отображается диалоговое окно с сообщением
#         # будет кнопка "перейти" с ссылкой
#         request.context = {
#             'data': {},
#             'message': None,  # text only or {'title': 'test', 'text': 'test'}
#             'error': False,
#             'redirect_by_button': '',
#             'redirect': '',
#             'reload_state': False,
#             'reload': False,
#         }
#
#         self.storage.set_ip(request)
#
#         if not hasattr(view_func, 'initkwargs'):
#             self.storage.reset()
#             return
#
#         request.account = None
#         translation.activate(request.META.get('HTTP_ACCEPT_LANGUAGE') or 'uk')
#         request.LANGUAGE_CODE = translation.get_language()
#         request._ = _  # gettext
#
#         request_url = request.META.get('PATH_INFO')
#
#         request_method = request.method
#
#         is_login = view_func.initkwargs.get('isLogin', True)
#
#         if not is_login:
#             self.logger.info(
#                 '{} anonymous_request {} {}'.format(self.storage.ip, request_url, request.body.decode('utf-8') or ''))
#             return
#
#         token = request.META.get('HTTP_AUTHORIZATION', None)
#         error = {'message': 'Not authorized'}
#
#         if not token:
#             self.storage.reset()
#             return JsonResponse(error, status=status.HTTP_401_UNAUTHORIZED)
#
#         token = token.replace('JWT ', '')
#
#         decode_token = self.decode_token(token)
#         if not decode_token:
#             self.storage.reset()
#             return JsonResponse(error, status=status.HTTP_401_UNAUTHORIZED)
#
#         account_id = decode_token.get('account_id')
#         if not account_id:
#             self.storage.reset()
#             return JsonResponse(error, status=status.HTTP_401_UNAUTHORIZED)
#
#         request.account = self.storage.get_account(pk=account_id)
#         request.point = self.storage.get_point(request.account, decode_token)
#
#         if not request.point:
#             request.context['message'] = _('Обрана точка не знайдена')
#             return JsonResponse(request.context, status=status.HTTP_401_UNAUTHORIZED)
#
#         if 'feedback' not in request_url:
#             self.logger.info('{} {} {} {}'.format(
#                 self.storage.ip,
#                 request.account.agg_id, request_url, request.body.decode('utf-8') or ''))
#
#         # We aren't give access for MNA users
#         if self.storage.is_mna(request.account) and request_method in ('POST', 'PUT'):
#             allowed_urls_pattern = r'api\/v2\/feedback|api\/v2\/notifications|' \
#                                    r'api\/v2\/statistic\/|services\/credit_trust\/|' \
#                                    r'api\/v2\/pay_systems\/'
#             if not re.search(allowed_urls_pattern, request_url):
#                 self.logger.info('[%s] %s error. MNA user was blocked' % (
#                     request.account.agg_id, status.HTTP_400_BAD_REQUEST))
#
#                 request.context['message'] = request._(
#                     'Шановний абонент! У Вас не оформлений договір на надання послуг з компанією IPnet. '
#                     'Будь ласка, зверніться з документами до центру обслуговування абонентів IPnet за адресами:'
#                     ' <a href="https://ipnet.ua/contacts" target="_blank">https://ipnet.ua/contacts</a>')
#                 return JsonResponse(request.context, status=status.HTTP_400_BAD_REQUEST)
#
#     def process_response(self, request, response):
#         token = request.META.get('HTTP_AUTHORIZATION', None)
#         if not token:
#             return response
#         token = token.replace('JWT ', '')
#         decode_token = self.decode_token(token)
#
#         if not decode_token:
#             error = {'message': 'Not authorized'}
#             return JsonResponse(error, status=status.HTTP_401_UNAUTHORIZED)
#
#         if getattr(request, 'account', None):
#             self.logger.info('request_total_time {} secs {} {}'.format(
#                 time() - self.request_time,
#                 request.account.agg_id, request.META.get('PATH_INFO')))
#         else:
#             self.logger.info('request_total_time {} secs {}'.format(time() - self.request_time,
#                                                                     request.META.get('PATH_INFO')))
#         return response