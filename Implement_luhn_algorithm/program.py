def verify_card_number(number_card: str):
    if '-' in number_card:
        number_card = number_card.replace('-', '')
    if ' ' in number_card:
        number_card = number_card.replace(' ', '')
    nums = list(number_card)
    
    for i in range(len(nums)-2, -1, -2):
        nums[i] = int(nums[i])
        nums[i] *= 2
        if nums[i] > 9:
            nums[i] -= 9
        nums[i] = str(nums[i])
    
    sums = 0
    for num in nums:
        num = int(num)
        sums += num
    if sums % 10 == 0:
        return 'VALID!'
    else:
        return 'INVALID!'



print(verify_card_number('453914889'))
print(verify_card_number('4111-1111-1111-1111'))
print(verify_card_number('453914881'))
print(verify_card_number('1234 5678 9012 3456'))
