totalNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
givenNumber = [ 4, 8]

balanceNumber = [num for num in totalNumber if num not in givenNumber]

print("Balance Numbers:", balanceNumber)
