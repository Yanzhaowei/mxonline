# -*-coding: utf-8 -＊-
__author__ = 'zyw'
__date__ = '18-2-13 下午8:40'

import xadmin
from .models import EmailVerifyRecord, Banner
# 导入试图注册主题
from xadmin import views



# xadmin的全局配置
class BaseSetting(object):
    # 设置主题，默认是关闭的，
    # 设置为true后可以提供一个主题的选项框，
    enable_themes = True
    use_bootswatch = True

# 注册全局设置，　主题
xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSettings:
    site_title = 'mx后台管理系统' # 设置title
    site_footer = 'mobile_learn' # 设置footer
    menu_style = 'accordion' # 设置折叠
xadmin.site.register(views.CommAdminView, GlobalSettings)



class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']



class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)




