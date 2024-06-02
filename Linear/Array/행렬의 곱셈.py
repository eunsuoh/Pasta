def solution(arr1, arr2):
  #행렬 arr1과 arr2의 행과 열의 수
  row1, col1 = len(arr1), len(arr1[0])
  row2, col2 = len(arr2), len(arr2[0])
  ret = [[0] * col2 for _ in range(row1)]
  for i in range(row1):
    for j in range(col2):
      for k in range(col2):
        for k in range(col1):
          ret[i][j] += arr1[i][k] * arr2[k][j]
  return ret

arr1 = [[1,2],[3,4],[5,6]]
arr2 = [[7,7],[8,8]]

solution(arr1, arr2)
