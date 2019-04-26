from Common import Request, Assert,read_excel,Login
import allure
import pytest

request = Request.Request()
assertion = Assert.Assertions()

idsList=[]

excel_list = read_excel.read_excel_list('../document/tuihuo.xlsx')
length = len(excel_list)
for i in range(length):
    idsList.append(excel_list[i].pop())

url = 'http://192.168.1.137:8080/'
head = {}
item_id=0

@allure.feature('商品退货模块')
class Test_tuihuo:

    @allure.story('查询列表')
    def test_get_data_list(self):
        global head
        head = Login.Login().get_token()
        get_data_list_resp = request.get_request(url=url + 'returnReason/list', params={'pageNum': 1, 'pageSize': 5}, headers=head)
        get_json = get_data_list_resp.json()

        json_data = get_json['data']
        data_list = json_data['list']
        item = data_list[0]
        global item_id
        item_id = item['id']
        assertion.assert_code(get_data_list_resp.status_code, 200)
        assertion.assert_in_text(get_json['message'], '成功')

    @allure.story('删除优惠券')
    def test_del_list(self):
        del_resp = request.post_request(url=url + 'returnReason/delete?ids='+str(item_id), headers=head)
        resp_json = del_resp.json()
        assertion.assert_code(del_resp.status_code, 200)
        assertion.assert_in_text(resp_json['message'], '成功')

    @allure.story('批量添加优惠券')
    @pytest.mark.parametrize("name,msg", excel_list, ids=idsList)
    def test_add_list(self, name, msg):
        json = {"name": name, "sort": 0, "status": 1, "createTime": ''}
        add_resp = request.post_request(url=url + 'returnReason/create', json=json, headers=head)
        resp_json = add_resp.json()
        assertion.assert_code(add_resp.status_code, 200)
        assertion.assert_in_text(resp_json['message'], msg)
