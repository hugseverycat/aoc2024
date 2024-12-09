with open('input/09.txt') as f:
    disk_map = [int(x) for x in [line.rstrip() for line in f][0]]

current_id = len(disk_map)//2
front_id = 0
compact = [front_id, disk_map.pop(0)]  # Compact will be file id, length, file id, length, etc.
front_id += 1

while disk_map:
    # The first character represents the length of free space
    # Going to get the last character, which should be a file with file ID current_id
    current_file = disk_map[-1]
    if len(disk_map) == 2:  # Last file
        compact += [current_id, current_file]
        break

    # Can the file fit entirely into the free space we have available, with room to spare?
    if current_file < disk_map[0]:
        #print(f"File ID {current_id} with length {current_file} fits entirely into {disk_map[0]}")
        # Update the free space in the front of disk_map
        disk_map[0] -= current_file
        # Add current_file to compact
        compact += [current_id, current_file]
        # Update the current_id
        current_id -= 1
        # Clean up the file and extra free space at the end of disk_map
        disk_map.pop()  # File
        disk_map.pop()  # Free space
    # Can the file fit exactly into the free space, with no room to spare?
    elif current_file == disk_map[0]:
        #print(f"File ID {current_id} with length {current_file} fits perfectly into {disk_map[0]}")
        # Remove the free space in the front of disk_map
        disk_map.pop(0)
        # Add current_file to compact and update the current_id
        compact += [current_id, current_file]
        current_id -= 1
        # Clean up the file and extra free space at the end of disk_map
        disk_map.pop()  # File
        disk_map.pop()  # Free space

        # Move the front file into compact and update the front_id
        compact += [front_id, disk_map.pop(0)]
        front_id += 1
    # Else, the file needs to be split up
    else:
        #print(f"File ID {current_id} with length {current_file} fits partially into {disk_map[0]}")
        # Add part of the current_file to compact. Do not update current_id
        compact += [current_id, disk_map[0]]
        # Update current_file to reflect its remaining length
        current_file = current_file - disk_map[0]
        # Remove the free space in the front of disk_map
        disk_map.pop(0)
        # Move the front file into compact and update the front_id
        compact += [front_id, disk_map.pop(0)]
        front_id += 1
        # Update the current_file length in disk_map for the next iteration
        disk_map[-1] = current_file

counter = 0  # Keeps track of the overall index
check_sum = 0
for i in range(len(compact)//2):  # Going through compact in groups of 2
    file_id = compact[i*2]
    count = compact[i*2 + 1]
    for c in range(count):
        check_sum += file_id * counter
        counter += 1
print(check_sum)