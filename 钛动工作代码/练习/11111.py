app_all_dict = [
    # 采集
    {"app_singular_crawler": 1, "app_login_singular": 3},
    {"app_aliexpress_crawler": 2, "app_login_aliexpress": 4}
    # 登录
]

appNames = ["app_singular_crawler", "app_aliexpress_crawler"]


class GetApp:
    def __init__(self):
        super().__init__()
        self.app_name = None

    def get_appname(self):
        for self.app_name in appNames:
            yield self.app_name

    def get_name(self):
        app_dicts = self.get_appname()
        for app_dict in app_dicts:
            # print(type(app_dict))
            print(app_dict)


a = GetApp()
a.get_name()
