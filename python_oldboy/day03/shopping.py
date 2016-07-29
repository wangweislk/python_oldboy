# _*_ coding:utf-8 _*_

def get_customer_salary():
    while True:
        salary = raw_input("Please your salary:")
        try:
            return float(salary)
            break
        except Exception,e:
            print "输入工资错误，请从新输入!"

def show_shopping_list(cart):
    print "\t 商品名称 \t\t 商品数量"
    for k,v in cart.items():
        print "\t %s \t\t %d" % k,v

if __name__ == '__main__':
    #获取工资
    salary = get_customer_salary()
    total_money = salary
    #初始化购物车
    cart = {}
    while True:
        #打印购物车商品
        show_shopping_list(cart)

