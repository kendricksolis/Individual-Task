'''Module 4: Individual Programming Assignment 1
Parsing Data
This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    This function describes the relationship that two users have with each other.
    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    from_member_following= social_graph[from_member]["following"]
    to_member_following= social_graph[to_member]["following"]
    for a,b in enumerate(from_member_following):
        if b == to_member:
            for c,d in enumerate(to_member_following):
                 if c < len(to_member_following):
                    if d == from_member:
                        return "friends"
                    else:
                        continue
            return "follower"
        else:
            continue
    else:
        break
    for c,d in enumerate(to_member_following):
        if c== from_member:
            return "followed by"
        else:
            continue
    else:
        return "no relationship"          

def tic_tac_toe(board):
    horizontal_check = [x for x in board]
    vertical_check = [x for x in zip(*board)]
    updown_diagonal_check = [board[i][i] for i in range(len(board))]
    downup_diagonal_check = [board[len(board)-1-i][i] for i in range(len(board))]
    
    for j,m in enumerate(horizontal_check):
        if j < len(horizontal_check):
            if all([s=="X" for s in m]):
                return "X"
            elif all([s=="O" for s in m]):
                return "O"
            else:
                continue
        else:
            break
                      
    for l,n in enumerate(vertical_check):
        if l < len(vertical_check):
            if all([s=="X" for s in n]):
                return "X"
            elif all([s=="O" for s in n]):
                return "O"
            else:
                continue
        else:
            break
                      
    if all([s=="X" for s in updown_diagonal_check]):
          return "X"
    elif all([s=="O" for s in updown_diagonal_check]):
          return "O"
    elif all([s=="X" for s in downup_diagonal_check]):
          return "X"
    elif all([s=="O" for s in downup_diagonal_check]):
          return "O"
    else:
          return "NO WINNER"    

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass