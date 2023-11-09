import json
import os
from dotenv import find_dotenv, load_dotenv
from utils import get_info

load_dotenv(find_dotenv('.env'))
env_dist = os.environ

url_dict = {
    "getProjectInfo": "/TbProject/FindProjectByProjectNo?ProjectNo={}",
    "getProjectInfoDetail": "/TbProject/FindByProjectNo?ProjectNo={}",
    "getAllUid": "/common/queryuser",
    "getUserDetailByUid": "/TbUserResearch/FindByUserNo?UserNo={}"
}


def get_system_all_uid():
    # note: calling this func can retrieve all user id in this system
    url = url_dict['getAllUid']
    return json.loads(get_info(url))


def get_system_user_details_by_uid():
    # Note: calling this function can retrieve all user information(including sensitive information) in this system.
    # The execution speed may vary depending on the network speed, and it is expected to be time-consuming.
    uid_list = get_system_all_uid()
    user_detail_list = []
    for item in uid_list:
        uid = item['value']
        url = url_dict['getUserDetailByUid'].format(uid)
        res = get_info(url)
        user_detail_list.append(res)
    return json.dumps(user_detail_list)


def get_project_info_by_year(year=23, get_details=False):
    # Note: calling this function can retrieve all user project information(include details) in this system.
    # If project details are required, you can set get_details to True.
    # The execution speed may vary depending on the network speed, and it is expected to be time-consuming.
    project_list = []
    min_index = 100
    # max_index = 4000
    max_index = 120
    for item in range(min_index, max_index):
        project_no = str(year) + "Y" + str(item)
        print(project_no)
        url = url_dict['getProjectInfo'].format(project_no)
        res = get_info(url)
        if res == "[]":
            continue
        else:
            if get_details:
                url_detail = url_dict['getProjectInfoDetail']
                res_detail = get_info(url_detail)
                res = json.loads(res)
                res["project_detail"] = res_detail
            project_list.append(res)
    return json.dumps(project_list)


if __name__ == '__main__':
    # print(get_system_all_uid())
    get_system_user_details_by_uid()
