#***************************
# summary: used yield(), sys.getsizeof(), try/excepti, 
#          generator functions and generator expressions,
#          using multiple yield statements in a generator function,
#          .send(), .throw(), .stop() methods of generator.    
#***************************

# Reading large files
#------------------------------------------------
# reading and storing all the data in a list ----> fills memory ---> not good while dealing with large files.
# if the file was large, you'd get MemoryError.
def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result

csv_gen = csv_reader("some_csv.txt")
row_count = 0

for row in csv_gen:
    row_count += 1

print(f"Row count is {row_count}")
#------------------------------------------------

# created a generator function,which reads only one row at a time and 
# doesn't store all the row at once ---->memory efficient----> avoids MemoryError.
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row
csv_gen=csv_reader(file_name)
# OR use generator comprehension just like list comprehension
csv_gen = (row for row in open(file_name))

row_count=0
for r in row:
    row_count+=1 
print(f"Row count is {row_count}") 
#------------------------------------------------ 


# creating an infinite sequence
#------------------------------------------------ 
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
# do this 
for num in infinite_sequence:
    print(num,end=' ')
# or do this
gen=infinite_sequence()
for num in range(100):
    print(next(gen))
#------------------------------------------------


# Profiling generator performance
#------------------------------------------------ 
import sys

num_squared=[x**2 for x in range(10000)]
sys.getsizeof(num_squared)

num_squared=(x**2 for x in range(10000))
sys.getsizeof(num_squared)
# understand that if the size of the list is smaller than the memory (ram)
# then using list will lead to faster execution of the code.
# so use generators/lists accordingly depending on whether the constrains is on time or on memory.
#------------------------------------------------

# notice: if you keep on iterating of generator, you'll eventually exhaust the generator 
# and hit the StopIteration Error. To avoid this, you can use exeptions.
letters = ["a", "b", "c", "y"]
it = iter(letters)
while True:
    try:
        letter = next(it)
    except StopIteration:
        break
    print(letter)
#------------------------------------------------ 


# getting columns of a file row-wise by using generators 
#------------------------------------------------ 
file_name = "somefile.dat"
lines = (line for line in open(file_name)) # 1st generator/iterator
list_line = (s.rstrip().split(",") for s in lines) #2nd generator/iterator
# since generally the first row is the header/column names, 
# we can get the column names like this:
cols = next(list_line)
# then save the data as per the column names:
company_dicts = (dict(zip(cols, data)) for data in list_line) # 3rd generator/iterator
 
# in place of this function you can extract any information depending on the file you're using.
# the essencse of this generator is that you can iterae over a file's information the way you want.
funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
) # 4th gerenator

# Remember, you aren’t iterating through all these at once in the generator expression.
# In fact, you aren’t iterating through anything until you actually use a for loop or a function that works 
# on iterables, like sum(). In fact, call sum() now to iterate through the generators:

total_series_a = sum(funding)

'''
This script pulls together every generator you’ve built, and they all function as one big data pipeline. Here’s a line by line breakdown:

Line 2 reads in each line of the file.
Line 3 splits each line into values and puts the values into a list.
Line 4 uses next() to store the column names in a list.
Line 5 creates dictionaries and unites them with a zip() call:
The keys are the column names cols from line 4.
The values are the rows in list form, created in line 3.
Line 6 gets each company’s series A funding amounts. It also filters out any other raised amount.
Line 11 begins the iteration process by calling sum() to get the total amount of series A funding found in the CSV.
'''
