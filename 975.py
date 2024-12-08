def oddEvenJumps(A):
    N = len(A)
    odd_next, even_next = [0] * N, [0] * N

    # Initialize sorted stack
    stack = []
    for a, i in sorted([a, i] for i, a in enumerate(A)):
        while stack and stack[-1] < i:
            odd_next[stack.pop()] = i
        stack.append(i)

    # Initialize sorted stack
    stack = []
    for a, i in sorted([-a, i] for i, a in enumerate(A)):
        while stack and stack[-1] < i:
            even_next[stack.pop()] = i
        stack.append(i)

    odd_reachable = [0] * N
    even_reachable = [0] * N
    odd_reachable[-1] = even_reachable[-1] = 1

    for i in reversed(range(N-1)):
        odd_reachable[i] = even_reachable[odd_next[i]]
        even_reachable[i] = odd_reachable[even_next[i]]

    return sum(odd_reachable)

# Test example
A = [10, 13, 12, 14, 15]
print(oddEvenJumps(A))  # Output should be 2