def perform_operation(num1, num2, operation):
    if operation =='add': 
        result = num1 + num2
        return float(result)
    elif operation == 'subtract':
        result = num1 - num2
        return float(result)
    elif operation == 'multiply':
        result = num1 * num2
        return float(result)
    elif operation == 'divide':
        if num2 == 0:
            print('Sorry, we cannot make this operation.')
        else:
            result = num1 / num2
            return float(result)


    
