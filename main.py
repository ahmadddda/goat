from football import get_uk_university_by_ranking, get_football_club_by_ranking
import grade_calculator
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




# Test the function with examples
print("\n--- UK University Ranking Lookup ---")
print(f"Ranking 1: {get_uk_university_by_ranking(1)}")
print(f"Ranking 3: {get_uk_university_by_ranking(3)}")
print(f"Ranking 10: {get_uk_university_by_ranking(10)}")
print(f"Ranking 50: {get_uk_university_by_ranking(50)}")
print(f"Ranking 100: {get_uk_university_by_ranking(100)}")

# Feature: Get Football Club by Ranking

# Test the function with examples
print("\n--- Top 50 Football Clubs Ranking Lookup ---")
print(f"Ranking 1: {get_football_club_by_ranking(1)}")
print(f"Ranking 5: {get_football_club_by_ranking(5)}")
print(f"Ranking 20: {get_football_club_by_ranking(20)}")
print(f"Ranking 35: {get_football_club_by_ranking(35)}")
print(f"Ranking 50: {get_football_club_by_ranking(50)}")

# Grade Calculator
print("\n--- Grade Calculator ---")
grade_calculator.main()


print("inshallah we get an a* and go to imperial")
