# coding:utf-8
import requests

import json
import os


class invoke_api:


    def __init__(self):
        self.api_key = "1e4491f9ec697e92d199d46dcb4257e4eb8630579c7fe2d958a90b6139e52271"
        self.upload_url = "https://www.virustotal.com/vtapi/v2/file/scan"
        self.rescan_url = "https://www.virustotal.com/vtapi/v2/file/rescan"
        self.report_url = "https://www.virustotal.com/vtapi/v2/file/report"

    def upload_file(self, file_name):

        params = {'apikey': self.api_key }
        files = {'file': (file_name, open(file_name, 'rb'))}


        response = requests.post(self.upload_url, files=files, params=params)
        upload_response = response.json()
        return upload_response

    def get_file_report(self):

        final_report = {}
        params = {'apikey': self.api_key,
                  'resource': '0496f4962d3dce3caa849f605749f7f2'}
        headers = {
            "Accept-Encoding": "gzip, deflate",
            "User-Agent": "gzip,  My Python requests library example client or username"
        }
        response = requests.get(self.report_url,
                                params=params, headers=headers)

        if (response.status_code == 200) and (response != []):

            json_response = dict(response.json())
            one_record = json_response.get('scans')
            one_forti_record = one_record.get('Fortinet')
            final_report['MD5'] = params['apikey']
            final_report['Detect_name'] = one_forti_record['result']
            number_of_engines = 0
            for each_engine_name, each_engine_value in one_record.iteritems():
                if each_engine_value['detected'] != 'false':
                    number_of_engines = number_of_engines + 1
            final_report['number_engines'] = number_of_engines
            return final_report
        else:
            return response.status_code






if __name__ == "__main__":
    a = invoke_api()
    print a.upload_file('example.txt')

    print a.get_file_report()