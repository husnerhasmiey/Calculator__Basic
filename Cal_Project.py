def calculator():
   
  Firstno=float(input("enter a number: ")) 
  Secondno=float(input("enter another number:"))
  operation=(input("choose specified operation:+,-,*,/.."))
   
  if operation=="+":
   result=Firstno + Secondno
   answer=result
   print(answer)
  elif operation=="-":
   result=Firstno - Secondno
   answer1=result
   print(answer1)
  elif operation=="*":
    result= Firstno*Secondno
    answer2=result
    print(answer2)
  elif operation=="/":
     result=Firstno/Secondno
     answer3=result
     print(answer3)
  else:
     print("incorrect input")
     return f"the result is:,{result}"

calculator()