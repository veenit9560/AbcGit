# if statement functions
print('Enter Marks :')
numbers=int(input())

# and function are both side condition are true then result True

if numbers>90 and numbers<=100:
    grade='A+'
elif numbers>=80 and numbers<90:
    grade='A'
elif numbers>=70 and numbers<=65:
    grade='B+'
elif numbers>=60 and numbers<65:
    grade='B'
elif numbers>=50 and numbers<60:
    grade='C'
else:
    grade=" Dont Know Your Grade in Marks "
print("This is your Grade",grade)
    
    