To_Do = {"虞姬": 888, "貂蝉": 1888, "克拉拉": 18888, "林志玲": 88888, "迪丽热巴": 99999} #@字典
print(To_Do.get("克拉", 22))   #@第二个参数是默认值，找不到就是这个值
To_Do["傻子"] = 9999999  #@字典的访问是【】，舔改也是【】
#@clear 和 del 有区别，后者直接删除了字典，无法访问

