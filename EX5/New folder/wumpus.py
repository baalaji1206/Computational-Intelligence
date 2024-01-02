def get_environment ( ):
  row , col = input ( "environment dimension: " ).split ( )
  return [ [ input ( "stuffs in " + str ( i ) + " , " + str ( j ) + ": " ).split ( )
  for j in range ( int ( col ) ) ] for i in range ( int ( col ) ) ]

def formMatrix ( shape , crow , ccol, environment ):
  format = [ [ '-' for i in range ( shape [ 1 ] ) ] for j in range ( shape [ 0 ] ) ]
  format [ crow ] [ ccol ] = '*'
  env = []
  for i in environment:
    env.append(i)
  #env[crow][ccol]+=['A']
  for rowi in format:
    for element in rowi:
      print ( element , end = " " )
    print ( )

def print_situation ( situation ):
  print ( "Agent " + ( "fell in the P" if situation == "P" else "feeds him to Wumpus" ) )

import random
def play ( start , environment , shape ):
  score = 1000
  crow , ccol = start
  experience = { '-' :set(), "S": set () , "B": set () , "notokay": set() ,
   "V": [ ] , "previous": [ ] }

  while ( "Gl" not in environment [ crow ] [ ccol ] ):
    formMatrix ( shape , crow , ccol, environment )
    print ( "Current Perception: " , environment [ crow ] [ ccol ][0] )
    perceived_values = environment [ crow ] [ ccol ]

    for situation in perceived_values:
      if ( situation not in experience ):
        print_situation ( situation )
        return
    current_possible_moves = set ( get_possible_moves ( ( crow , ccol ) , shape ) )

    if ( ( crow , ccol ) in current_possible_moves ):
     current_possible_moves.remove ( ( crow , ccol ) )
    for item in experience[ "V" ]:
      if ( item in current_possible_moves ):
        current_possible_moves.remove ( item )
    if ( "-" not in perceived_values ): #agent perceives - environment
      for situation in perceived_values:
        experience [ situation ].add ( ( crow  , ccol ) )
        copy = list ( current_possible_moves )
        for position in copy:
          next_possible_moves = get_possible_moves ( position , shape )
          next_possible_moves.remove ( ( crow , ccol ) )
          if ( not okay ( next_possible_moves , experience , situation ) ):
            current_possible_moves.remove ( position )
    copy = list ( current_possible_moves )
    for position in copy:
      if ( position in experience [ "notokay" ] ):
        current_possible_moves.remove ( position )
    if ( ( crow , ccol ) not in experience [ "V" ] ):
      experience [ "V" ].append ( ( crow , ccol ) )
    print ( "Next Possible Moves: " , current_possible_moves )
    if ( not len ( current_possible_moves ) ): #agent has no possible moves to continue
      if ( not len ( experience [ "previous" ] ) ):#no already V cell, agent has no solution now

           return
      experience ["notokay"].add((crow,ccol))
      crow , ccol = experience [ "previous" ].pop()
      print ("Back tracked to:" , (crow,ccol))
      continue
    # print ( "iam in " , ( crow , ccol ) , ", moves are " , current_possible_moves )
    if((crow,ccol) not in experience["previous"]):
      experience ["previous"].append((crow,ccol))
    crow , ccol = random.choice ( list ( current_possible_moves ) )
    print ( "Agent choses: " , ( crow , ccol ) )
    score -= 10
  print ( "G Found at: " , ( crow , ccol ) , " agent's score: " , score )

  formMatrix ( shape , crow , ccol,environment )

  print ( "Number of steps taken by agent: " , ( 1000 - score ) // 10 )

def okay ( surroundings , experience ,  situation ):
  for position in surroundings:
    if ( position in experience [ "V" ] ):
      if ( position not in experience [ situation ] ):
        return True
  return False

def get_possible_moves ( current_location , shape ):
  locations = [ ( current_location [ 0 ] + 1 , current_location [ 1 ] ) ,
   ( current_location [ 0 ] - 1 , current_location [ 1 ] ) ,
   ( current_location [ 0 ] , current_location [ 1 ] + 1 ) ,
   ( current_location [ 0 ] , current_location [ 1 ] - 1 ) ]
  return [ location for location in locations if ( is_valid ( location , shape ) ) ]

def is_valid ( location , shape ):
  return ( location [ 0 ] >= 0 ) and ( location [ 1 ] >= 0 ) and ( location [ 0 ] < shape [ 0 ] ) and ( location [ 1 ] < shape [ 1 ] )

environment1 = [ [ [ "S" ] , [ "-" ] , [ "B" ] , [ "P" ] ] ,
[ [ "W" ] , [ "B" , "S" , "Gl" , "G" ] , [ "P" ] , [ "B" ] ] ,
[ [ "S" ] , [ "-" ] , [ "B" ] , [ "-" ] ] ,
[ [ "-" ] , [ "B" ] , [ "P" ] , [ "B" ] ] ]

play ( ( 3 , 0 ) , environment1 , ( 4 , 4 ) )