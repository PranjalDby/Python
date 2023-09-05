class Meta(type):
    def __new__(self,class_name,bases,attrs):
        a={}
        for name,item in attrs.items():
            print(name)
            if(name.startswith("__")):
                a[name] = item
            else:
                a[name.upper()] = item
        return type(class_name,bases,attrs)