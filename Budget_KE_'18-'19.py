import matplotlib.pyplot as plt
class Budget:
    def __init__(self):
        #Initializes with an empty dictionary
        self.al= dict()
        self.total_b = 2556.6
        
        
    def ad_al(self,name, amount):
        #Adds allocations to main dictionary
        self.al[name]= amount*1000000000
    
    def pr_al(self):
        #Presents budget in a pretty form
        m="-"*50
        print(f"{m}\nTotal budget being Ksh {int(self.total_b*1000000000):,d}\n{m}\
              \nThe Allocations for 2018/19 Financial Year is as below:\n")
        num=1
        labels= ()
        explode= ()
        sizes=[]
        for i,k in self.al.items():
            print(f"{num}.  {i}:  Ksh {int(k):,d}")
            num+=1
            labels= labels + (i,)
            sizes.append(k)
            if i == "Environment Pro-tection, Water & Natural Resources":
                explode=  explode + (0.1,)
            elif k/(self.total_b*1000000000)*100 >15:
                explode=  explode + (0.1,)
            else:
                explode=  explode + (0,)

        plt.pie(sizes, explode=explode, labels=labels, colors=None,
        autopct='%1.1f%%', shadow=False, startangle=140)
        plt.axis('equal')
        plt.show()

b = Budget()
b.ad_al("Health", 90)
b.ad_al("Education", 444.1)
b.ad_al("Public Admin & International Relations", 270.1)
b.ad_al("County Shareable Revenue",314.0 )
b.ad_al("Governance, Justice, Law and Order",190.4 )
b.ad_al("Social Protection, Culture and Recreation",44.4 )
b.ad_al("CFS & Net lending (excl. domestic bond redemptions)",493)
b.ad_al("Economic and Commercial Affairs",25.4)
b.ad_al("Environment Pro-tection, Water & Natural Resources",77)
b.ad_al("Energy, Infrastructure & ICT",418.8)
b.ad_al("Agriculture, Rural & Urban Development",47.1)
b.ad_al("National Security",142.3)
b.pr_al()

