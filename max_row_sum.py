def max_row_sum(lst):
  if not lst:
    return (0)
  final = -50
  for i in range(len(lst)):
    count = 0 
    for j in range(len(lst[i])):
      count += lst[i][j]
    if count >= final:
      final = count
  return (final)
