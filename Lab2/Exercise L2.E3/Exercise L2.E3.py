# Exercise L2.E3

x=int(input('Units of electricity (number of kWh) consumed monthly: '))
if x<0:     # Minus units are invalid
    print('Invalid consumption units. Try again.')
else:
    if x<=60:   # If the consumption is between 0-60 kWh per month 
        if x<=30:
            amount=(x*30)+400
        else:
            amount=(30*30)+((x-30)*37)+550
    else:   # If the consumption is above 60 kWh per month
        if x<=60:
            amount=x*42
        elif x>=61 and x<=90:
            amount=(x*42)+650
        elif x>=91 and x<=120:
            amount=((90*42)+((x-90)*50))+1500
        elif x>=121 and x<=180:
            amount=((90*42)+(30*50)+((x-120)*50))+1500
        else:
            amount=((90*42)+(30*50)+(60*50)+(x-180)*75)+2000
    print('Rs',amount)  #Print the total amount
