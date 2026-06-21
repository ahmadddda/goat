print("This is the first line")
numbers = [1, 2,3, 4, 5,6, 7]
sum = 0
for number in numbers:

    squared = (number**2)
    sum += squared

print(sum)

print("This is the login feature")

print("VISC TIME lets test this out")
print("simultaneous equat")
print("hyperbolic functions")
print("how does this work")

branch = "chelsea"
if branch == "chelsea":
    print("chelsea is the best team in the world")
else:
    print("chelsea is not the best team in the world")

# Feature: Display top 10 UK Universities
def get_top_10_uk_universities():
    """Returns the current top 10 universities in the UK based on QS Rankings"""
    top_10_unis = [
        "University of Oxford",
        "University of Cambridge",
        "Imperial College London",
        "University College London (UCL)",
        "London School of Economics (LSE)",
        "University of Manchester",
        "University of Edinburgh",
        "University of Warwick",
        "Durham University",
        "University of Bath"
    ]
    return top_10_unis

print("\n--- Top 10 Universities in the UK ---")
universities = get_top_10_uk_universities()
for i, uni in enumerate(universities, 1):
    print(f"{i}. {uni}")