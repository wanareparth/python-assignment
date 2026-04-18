class acc:
    def __init__ (abc,acc_no,bal):
        abc.acc_no=acc_no
        abc.bal=bal
    def Acc_info(abc):
        print("Account no. is :",abc.acc_no)
        print("Balence is RS:",abc.bal)

    def withdraw(abc):
        With=int(input("Enter your Withdrawl amount :"))
        a=abc.bal
        a=a-With
        print(a)
    def deposite(abc):
        depo=int(input("enter your Deposite amount :"))
        b=abc.bal
        b=b+depo
        print(b)
acc1=acc(1153,150000)
acc1.Acc_info()
acc1.withdraw()
acc1.deposite()

