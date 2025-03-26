HomePage = 1
LinkPage = 1
External_1 = 1
External_2 = 1
LHome = 1
LLink = 3
LExternal_2 = 1
LExternal_1 = 1
LastHome = 1
LastLink = 1
LastExternal_1 = 1
LastExternal_2 = 1
num = 0


while True:
    HomePage = 0.15 + 0.85*(LinkPage/LLink + External_2/LExternal_2)
    LinkPage = 0.15+0.85*(HomePage/LHome)
    External_1 = 0.15+0.85*(LinkPage/LLink)
    External_2 = 0.15+0.85*(LinkPage/LLink)
    diff_home = HomePage - LastHome
    diff_link = LinkPage - LastLink
    diff_ex1 = External_1 - LastExternal_1
    diff_ex2 = External_2 - LastExternal_2
    sum_diff = diff_home + diff_link + diff_ex1 + diff_ex2
    if sum_diff == 0:
        break
    else:
        LastHome = HomePage
        LastLink = LinkPage
        LastExternal_1 = External_1
        LastExternal_2 = External_2
        num += 1
        print(HomePage, LinkPage, External_1, External_2)

print(f"Final Values:\n"
      f"HomePage: {HomePage}\n"
      f"LinkPage: {LinkPage}\n"
      f"External_1: {External_1}\n"
      f"External_2: {External_2}\n"
      f"Values stop changing after {num} iterations")
