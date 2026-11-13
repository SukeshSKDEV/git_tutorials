import os

gene_expression = [10, 20, 30, 40, 50]

total = sum(gene_expression)

average = total / len(gene_expression)

assert average == 32.0

print("Test passed: average is correct")
