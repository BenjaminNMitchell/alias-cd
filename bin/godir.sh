godir () {
    directory=$(alias-cd get $1)

    # if [ $? -eq 0 ]; then
    #     cd $directory
    #     return $?
    # else
    #     return -1
    # fi