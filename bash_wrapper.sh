alias_cd () {
    directory=$(python /Users/ben/Documents/Programming/Projects/alias-cd/src/alias_cd/cli.py get $1)
    if [ $? -eq 0 ]; then
        cd $directory
        return $?
    else
        return -1
    fi
