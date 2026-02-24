test_case = int(input())
for _ in range(test_case):
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        # Read as strings
        matrix.append(input().strip())
    
    layers_count = min(n, m) // 2
    total_counter = 0
    pattern = "1543"

    for k in range(layers_count):
        layer_elements = []
        # Top row (left to right)
        for j in range(k, m - k):
            layer_elements.append(matrix[k][j])
        # Right column (top to bottom)
        for i in range(k + 1, n - k):
            layer_elements.append(matrix[i][m - k - 1])
        # Bottom row (right to left)
        for j in range(m - k - 2, k - 1, -1):
            layer_elements.append(matrix[n - k - 1][j])
        # Left column (bottom to top)
        for i in range(n - k - 2, k, -1):
            layer_elements.append(matrix[i][k])
        
        # Join to string for easy searching
        s = "".join(layer_elements)
        # Add first 3 chars to the end to handle circular "1543"
        s += s[:3]
        
        # Count occurrences of 1543 in this specific layer
        for i in range(len(s) - 3):
            if s[i:i+4] == pattern:
                total_counter += 1
                
    print(total_counter)