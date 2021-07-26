def snail (array,arr=[])
  n = array.length 
  arr << array.shift
  (0..n-3).each { |i| arr << array[i].pop }
  arr << (array.empty? ? array.pop : array.pop.reverse)
  (n-3).downto(0) { |j| arr << array[j].shift }
  array.length>=2 ? snail(array,arr) : arr << array[0]
  arr.flatten.compact
end

# prueba = []
# prueba = [[1]]
# prueba = [[1,2],
#           [4,5],]
# prueba = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]
# prueba = [[1,2,3,5],
#           [4,5,6,7],
#           [7,8,9,1],
#           [4,5,6,7]]
# prueba = [[1,2,3,5,9],
#           [4,5,6,7,2],
#           [7,8,9,1,4],
#           [4,5,6,7,2],
#           [4,5,6,7,2]]
prueba = [[1,2,3,5,9,2],
          [4,5,6,7,2,1],
          [7,8,9,1,4,3],
          [4,5,6,7,2,9],
          [4,5,6,7,2,0],
          [4,5,6,7,2,0]]

p snail(prueba)