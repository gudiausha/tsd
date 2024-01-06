import ctypes


class Array():
  """
  Array implementation class
  """

  def __init__(self, size, datatype):
    """
    Initial Declaration Variables
    """
    self.item_count = 0
    self.array_capacity = size
    self.array_dt = datatype
    self.primary_array = self._create_array(self.array_capacity)

  def _create_array(self, array_capacity):
    """
    Creates new array with input capacity
    """
    return (array_capacity * ctypes.py_object)()

  def insert(self, item, index=None):
    """
    Add new item to array
    """
    # Check if array is full
    if self.item_count == self.array_capacity:
      print('Array limit reached')

    elif index is not None and 0 > index:
      print('Index out of bounds')

    # Check if index is not None
    elif isinstance(item, self.array_dt) and index is not None:
      move_counter = index
      # Check if index is not the last count
      if index != self.item_count:
        # Move all items to the right of the index
        while move_counter < self.array_capacity - 1:
          #using array_capacity-1 because array is starting from index0
          self.primary_array[move_counter +
                             1] = self.primary_array[move_counter]
          move_counter += 1

      # Insert item at index
      self.primary_array[index] = item
      self.item_count += 1

    # Check if index is None
    elif isinstance(item, self.array_dt) and index is None:
      self.primary_array[self.item_count] = item
      self.item_count += 1

    # Check if item is not of type array_dt
    else:
      print('Item is not of the declared array type')

  def delete(self, index=None):
    """
    Delete item from array
    """
    # Check if array index is available
    if index is not None:
      # Check if index is invalid
      if 0 > index or index > self.array_capacity - 1:
        print('Index out of range')

      # Check if index is not the last count
      elif index != self.item_count:

        # Move all items to the left of the index
        move_counter = index
        while (move_counter + 1) < self.array_capacity - 1:
          self.primary_array[move_counter] = self.primary_array[move_counter +
                                                                1]
          move_counter += 1
        self.item_count -= 1

      # If index is given and is the last count
      # Delete item at index
      else:
        self.item_count -= 1

    # Delete item at last index - Default case
    else:
      self.item_count -= 1

  def get_item(self, index):
    """
    List item at index k in array
    """
    # Check if index is valid
    if 0 > index or index >= self.array_capacity - 1:
      print('Input index out of range')
      print('The array is 0 indexed and length is ', self.array_capacity - 1)

    # Check if index is None
    elif index is None:
      print('Enter a valid index')

    # Check if valid item count
    # We are having this case because the values are not deleted from the array
    # we are only reducing the item count
    elif self.item_count == 0:
      print('Array is empty')

    # Return item at index
    else:
      print(self.primary_array[index])

  def search(self, item):
    """
    Linear Search for an item in the array
    """
    # Check if value is given
    if item is None:
      print('Enter a valid value')

    # Check if item is not of type array_dt
    elif not isinstance(item, self.array_dt):
      print('Value is not of the declared array type - ', self.array_dt)

    # Check if array is null
    elif self.item_count == 0:
      print('Array is empty')

    # Check if item is present in array
    else:
      # Iterate through array and return the index at the first occurence
      for i in range(self.item_count):
        if self.primary_array[i] == item:
          print('Value found at index ', i)
          break
      else:
        print('The Value is not available')

      # Iterate through array and return all the indices the value occurs
      # search_indices_list = ''
      # incrementor = 0
      # for i in range(self.item_count):
      #   if self.primary_array[i] == item:
      #     search_indices_list += str(i) + ' '
      #     incrementor += 1
      # if incrementor != 0:
      #   print('The Value is found at following indices', search_indices_list)
      # else:
      #   print('The Value is not available')

  def print_array(self):
    """
    List all items in array
    """
    array_str = ''
    for i in range(self.item_count):
      array_str += str(self.primary_array[i]) + ', '
    print(array_str)


x = Array(5, str)

