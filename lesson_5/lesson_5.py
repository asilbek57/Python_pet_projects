# ==============================================================
# Task 1
# Write a script that defines convert_cel_to_far() and
# convert_far_to_cel(), prompts the user for temperatures, and
# displays the converted values.
# ==============================================================

def convert_cel_to_far(d):
    f = d * 9/5 + 32
    return f


def convert_far_to_cel(fa):
    c = (fa - 32) * 5/9
    return c

d1 = float(input("Enter temperature in celcius: "))
print(f" {d1} C is {convert_cel_to_far(d1)} F")
fa1 = float(input("Enter temperature in fahrenheit"))
print(f" {fa1} F is {convert_far_to_cel(fa1)} C")


# ==============================================================
# Task 2
# invest.py - tracks the growing amount of an investment over time.
# ==============================================================

def invest(a, r, y):
    a1 = a
    year = 0
    for y in range(1, y + 1):
        a1 *= (1 + r)
        year += 1
        print(f" year {year} : {round(a1, 2)}")

aa = float(input("Enter your initial deposit"))
rr = float(input("Enter an annual percentage rate(.0num): "))
yy = int(input("Enter a number of years: "))
invest(aa, rr, yy)


# ==============================================================
# Task 3
# factors.py - asks the user for a positive integer and prints
# out its factors.
# ==============================================================

def factor():
    n = int(input("Enter a positive integer: "))
    for i in range(1, n + 1):
        if n % i == 0:
            print(f"{i} is a factor of {n}")

factor()


# ==============================================================
# Task 4
# enrollment_stats() / mean() / median() on a list of universities.
# ==============================================================

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(universities):
    values = []
    tuition = []
    for i in universities:
        values.append(i[1])
        tuition.append(i[2])

    for index, n in enumerate(values):
        print(f"Total Students in {universities[index][0]}: {n} students")
        print(f"Total tuition in {universities[index][0]}: ${tuition[index]}")
    return values, tuition

enrolled, fee = enrollment_stats(universities)
print(enrolled)
print(fee)


def mean(m):
    return (sum(m) / len(m))

def median(med):
    sorted_med = sorted(med)
    n = len(sorted_med)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_med[mid - 1] + sorted_med[mid]) / 2
    else:
        return sorted_med[mid]

median(enrolled)
mean(enrolled)

median(fee)
mean(fee)

total_enrolled = sum(enrolled)
total_fee = sum(fee)

student_mean = mean(enrolled)
student_median = median(enrolled)
tuition_mean = mean(fee)
tuition_median = median(fee)

print(f"Total students: {total_enrolled}; Total Fee: {total_fee} ")
print(f"Student mean: {round(student_mean, 2)} Student median: {round(student_median, 2)}\n")
print(f"Tuition mean: {round(tuition_mean, 2)} Tuition median: {round(tuition_median, 2)}")


# ==============================================================
# Task 5
# is_prime(n) - returns True if n is a prime number, else False.
# ==============================================================

def is_prime(n):
    prime = True
    for g in range(2, n):
        if n % g == 0:
            prime = False
    return prime

is_prime(6)
