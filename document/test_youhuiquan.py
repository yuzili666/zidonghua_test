from Common import Request, Assert, read_excel
import allure
import pytest

request = Request.Request()
assertion = Assert.Assertions()

idsList=[]
excel_list = read_excel.read_excel_list('../document/youhuiquan.xlsx')
length = len(excel_list)
for i in range(length):
    idsList.append(excel_list[i].pop())


url = 'http://192.168.1.137:8080/'
head = {}
youhuiquan_id=0

@allure.feature("登录功能")
class Test_yhq:

    @allure.story("登录")
    def test_login(self):
        # =后面 :  request对象 调用了  post_request  方法,传入了两个参数
        # = 前面:  将方法 返回的 对象/变量  起一个名字
        login_resp = request.post_request(url=url+'admin/login',
                                            json={"username": "admin", "password": "123456"})

        # 响应 . text  :  就是获取 text属性的内容,这个就是 响应正文 (str 格式)
        resp_text = login_resp.text
        print(type(resp_text))

        # 响应 .json()  :  就是获取 字典格式的内容,这个就是 响应正文 (字典 格式)
        resp_dict = login_resp.json()

        print(type(resp_dict))

        # .assert_code 用来断言 状态码 ; 第一个参数 填 响应的状态码, 第二个参数 期望值
        assertion.assert_code(login_resp.status_code,200)

        # .assert_in_text 用来断言字符 第一个参数填 比较多的那个字符; 第二参数填 这个字符 是否存在第一个字符里面
        assertion.assert_in_text(resp_dict['message'],'成功')



        data_dict = resp_dict['data']
        token = data_dict['token']
        tokenHead = data_dict['tokenHead']
        global head
        head ={ 'Authorization' : tokenHead+token}


    @allure.story('添加优惠券')
    def test_add_youhuiquan(self):
        req_json = {"type":0,"name":"iPhone X优惠券","platform":0,"amount":10,"perLimit":1,"minPoint":20,"startTime":'null',"endTime":'null',"useType":0,"note":'null',"publishCount":30,"productRelationList":[],"productCategoryRelationList":[]}
        add_resp = request.post_request(url=url + 'coupon/create', json=req_json, headers=head)
        add_json = add_resp.json()
        assertion.assert_code(add_resp.status_code,200)
        assertion.assert_in_text(add_json['message'],'成功')

        json_data = add_json['data']
        data_list_ = json_data['list']
        item = data_list_[0]
        global youhuiquan_id
        youhuiquan_id = item['id']

    # @allure.story('添加优惠券(参数化)')
    # @pytest.mark.parametrize("name,amout,minPonit,publishCount,",['test1','test2','test3'],ids=['面额10元,使用门槛20元,发行30张','面额20元,使用门槛50元,发行50张'])
    # def test_add_youhuiquan(self):
    #     req_json = {"type": 0, "name": "iPhone X优惠券", "platform": 0, "amount": 10, "perLimit": 1, "minPoint": 20,
    #                 "startTime": '', "endTime": '', "useType": 0, "note": '', "publishCount": 30,
    #                 "productRelationList": [], "productCategoryRelationList": []}
    #     add_resp = request.post_request(url=url + 'coupon/create', json=req_json, headers=head)
    #     add_json = add_resp.json()
    #     assertion.assert_code(add_resp.status_code, 200)
    #     assertion.assert_in_text(add_json['message'], '成功')

    @allure.story("删除优惠券")
    def test_del_youhuiquan(self):
        del_youhuiquan_resp = request.post_request(url=url + 'coupon/delete/' + str(youhuiquan_id), headers=head)
        resp_json1 = del_youhuiquan_resp.json()
        assertion.assert_code(del_youhuiquan_resp.status_code, 200)
        assertion.assert_in_text(resp_json1['message'], '成功')





