def main():
    n = int(input().strip())
    patients = []
    for i in range(n):
        name, plan, gravity = input().strip().split()
        plan_priority = 0
        if plan == 'premium':
            plan_priority = 5
        elif plan == 'diamante':
            plan_priority = 4
        elif plan == 'ouro':
            plan_priority = 3
        elif plan == 'prata':
            plan_priority = 2
        elif plan == 'bronze':
            plan_priority = 1
        patients.append((name, plan_priority, int(gravity)))
    sorted_patients = quick_sort(patients)
    for patient in sorted_patients:
        print(patient[0])

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = []
        equal = []
        greater = []
        for patient in arr:
            if patient[1] > pivot[1]:
                less.append(patient)
            elif patient[1] == pivot[1]:
                if patient[2] > pivot[2]:
                    less.append(patient)
                elif patient[2] == pivot[2]:
                    equal.append(patient)
                else:
                    greater.append(patient)
            else:
                greater.append(patient)
        return quick_sort(less) + equal + quick_sort(greater)

main()

