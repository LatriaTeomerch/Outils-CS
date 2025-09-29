#!/bin/bash

# Function to choose a random word from an array
get_random_word() {
    local array=("$@")
    local length=${#array[@]}
    local random_index=$((RANDOM % length))
    echo "${array[random_index]}"
}

# Function to generate a random number
get_random_number() {
    echo $((RANDOM % 1000))
}

# Function to create a themed random directory structure
create_random_dungeon() {
    local depth=$1
    local max_depth=$2
    local max_files=$3

    # Base case: if depth reaches the maximum, max_files is zero, or total_files is greater than 30, return
    if [ $depth -ge $max_depth ] || [ $max_files -eq 0 ] || [ $total_files -ge 30 ]; then
        return
    fi

    local room_names=("cellar" "chamber" "hall" "corridor")
    local monster_names=("goblins" "troll" "wyvern" "dragon")
    local loot=("swords" "treasure_chests" "axe")
    local monster_type=""

    local room_number=$(get_random_number)
    local room_name=$(get_random_word "${room_names[@]}")
    local room_dir="${room_name}_${room_number}"
    mkdir "$room_dir"
    cd "$room_dir"

    local num_files=$((RANDOM % max_files + 1))
    for ((i = 0; i < num_files; i++)); do
        if [ $total_files -ge 30 ]; then
            break
        fi

        monster_name=$(get_random_word "${monster_names[@]}")
        touch "${monster_name}.txt"

        # Determine if this is the monster with a prince/princess
        if [ "$monster_name" == "goblins" ]; then
            if [ $((RANDOM % 2)) -eq 1 ]; then
                monster_type=$(get_random_word "prince" "princess")
                echo "$monster_type" >"${monster_name}.txt"
            fi
        fi

        # Add loot to the file
        loot_item=$(get_random_word "${loot[@]}")
        echo "Loot: $loot_item" >>"${monster_name}.txt"

        total_files=$((total_files + 1))
    done

    for ((i = 0; i < max_files; i++)); do
        create_random_dungeon "$((depth + 1))" "$max_depth" "$((max_files / 2))"
    done

    cd ..
}

# Specify the depth of the directory structure and maximum files per directory
depth=3
max_files_per_directory=5
total_files=0  # Initialize the total files count

# Create the root directory "Dungeon"
root_dir="Dungeon"
mkdir -p "$root_dir"
cd "$root_dir"

# Start creating the themed random dungeon structure
create_random_dungeon 0 "$depth" "$max_files_per_directory"
cd ..
echo "Themed dungeon structure created in $root_dir"
