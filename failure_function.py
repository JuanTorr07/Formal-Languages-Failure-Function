def compute_failure_function(keyword):
    n = len(keyword)
    if n == 0:
        return []
        
    f = [0] * n 
    t = 0
    
    for s in range(1, n):
    
        while t > 0 and keyword[s] != keyword[t]:
            t = f[t - 1]
            
        if keyword[s] == keyword[t]:
            t = t + 1
            f[s] = t
        else:
            f[s] = 0
            
    return f

if __name__ == '__main__':
    strings = ["abababaab", "aaaaaa", "abbaabb"]
    
    print("Ejercicio 3.4.3:\n")
    for word in strings:
        result = compute_failure_function(word)
        print(f"Palabra: {word}")
        print(f"f(s):    {result}\n")