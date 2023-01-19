
```python
odd_nums = []

for num in range(10):
    if num%2 ==0:
        continue          #skips this iteration and starts the next iteration.
    odd_nums.append(num)
    
print(odd_nums)

#> [1, 3, 5, 7, 9]
```


```python
users = {'Éléonore': 'inactive','Hans': 'active', '景太郎': 'active'}

inactive_count = 0

for user, status in users.items():
	if status == 'active':
		print("active users found, do not perform maintainence")
		break                           #breaks entirely out of the for loop
	else:
		inactive_count += 1

if inactive_count == len(users):
	print("All users are inasctive, perform maintenance.")

#>active users found, do not perform maintainence
```


### __`else`__ after loops
---

>The else block just after for/while is executed only when the loop is NOT terminated by a break statement.

Making everyone inactive in the above illustration.
```python
users = {'Éléonore': 'inactive','Hans': 'inactive', '景太郎': 'inactive'}

for user, status in users.items():
	if status == 'active':
		print("active users found, do not perform maintainence")
		break                           #breaks entirely out of the for loop
else:
    print("All users are inactive, perform maintenance.")

#>All users are inasctive, perform maintenance.
```

Same code present above but using while loop (just shows how choosing the right loop makes the job so easy)
```python
users = {'Éléonore': 'inactive','Hans': 'inactive', '景太郎': 'inactive'}

enumerated = list(enumerate(users))  #[(0, 'Éléonore'), (1, 'Hans'), (2, '景太郎')]
index = 0

while index in (0,len(users)-1):
    if users[enumerated[index][1]] == 'active':
        print("active users found, do not perform maintainence")
        index += 1
        break
    else:
        index+=1
else:
    print("All users are inactive, perform maintenance.")
    
#>All users are inasctive, perform maintenance.
```


