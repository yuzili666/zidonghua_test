# from Common import Request, Assert,Tools
# import allure
# import pytest
#
# request = Request.Request()
# assertion = Assert.Assertions()
# phone = Tools.phone_num()
#
# url = 'http://192.168.1.137:1811/'
# head = {}
#
#
# phone = '18556359869'
# pwd = "y123455"
# rePwd = "y123455"
# userName = "yzl661"
#
#
# @allure.feature('注册模块')
# class Test_zhuce:
#
#
#     @allure.story('用户注册')
#     def test_zhuce(self):
#         json = {"phone": phone, "pwd": pwd, "rePwd": rePwd,
#                 "userName": userName}
#         post_resp = request.post_request(url = url + 'user/signup',json=json)
#
#         resp_json = post_resp.json()
#
#         assertion.assert_code(post_resp.status_code,200)
#         assertion.assert_in_text(resp_json["respDesc"],'成功')
#
#
#     @allure.story('用户登录')
#     def test_login(self):
#         json = {"userName": userName,"pwd": pwd}
#         post_resp = request.post_request(url=url + 'user/login', json=json)
#         resp_json = post_resp.json()
#
#         assertion.assert_code(post_resp.status_code, 200)
#         assertion.assert_in_text(resp_json["respDesc"], '成功')
#




from Common import Request,Assert,Tools
import allure
import pytest
request = Request.Request()
assertion = Assert.Assertions()

url='http://192.168.1.137:1811/'


phone= Tools.phone_num()
pwd=Tools.random_str_abc(3)+Tools.random_123(3)
newpwd=Tools.random_str_abc(3)+Tools.random_123(3)
rePwd=pwd
userName=Tools.random_str_abc(3)+Tools.random_123(4)



@allure.feature('用户模块接口')
class Test_zc:
    @allure.story('注册用户')
    def test_zc(self):
        json={"phone": phone, "pwd": pwd,"rePwd": rePwd,"userName": userName}
        post_request = request.post_request(url=url + 'user/signup', json=json)
        request_json = post_request.json()
        assertion.assert_code(post_request.status_code,200)
        assertion.assert_in_text(request_json['respBase'], '成功')


    @allure.story('登录用户')
    def test_loign(self):
        json={"pwd":pwd,"userName": userName}
        post_request = request.post_request(url=url + 'user/login', json=json)
        request_json = post_request.json()
        assertion.assert_code(post_request.status_code, 200)
        assertion.assert_in_text(request_json['respDesc'], '成功')

    @allure.story('修改密码')
    def test_adm(self):
        json={"newPwd":newpwd,"oldPwd": pwd,"reNewPwd": newpwd,"userName":userName}
        post_resp = request.post_request(url=url + 'user/changepwd', json=json, )
        resp_json = post_resp.json()
        assertion.assert_code(post_resp.status_code, 200)
        assertion.assert_in_text(resp_json['respDesc'], '成功')


    # @allure.story('用户冻结')
    # def test_lock(self):
    #     json = {'userName':userName}
    #     post_resp = request.post_request(url=url + 'user/lock', json=json,headers = {"Content-Type":"application/x-www-form-urlencoded"})
    #     resp_json = post_resp.json()
    #     assertion.assert_code(post_resp.status_code, 200)
    #     assertion.assert_in_text(resp_json['respDesc'], '成功')


