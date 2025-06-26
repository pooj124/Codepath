audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

def max_audience_performances(audiences):
    if not audiences:
        return 0
    
    max_aud = max(audiences)
    total = 0

    for size in audiences:
        if size == max_aud:
            total += size
    
    return total


print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))