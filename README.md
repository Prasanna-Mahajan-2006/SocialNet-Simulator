
# SOCIAL NET SIMULATOR

This project implements the basic functionality of a Social Network Application using the concepts of Data Structures and Algorithms

## Features

- Allows the creation/enrollment of new users
- Simulates efficiently the friend connections between users
- Suggests/Recommends friends based on mutual connections
- Efficiently time-stamps the posts created by users
- Robust error handling


## Documentation
This project has been implemented in C++17 and requires as a prerequisite a C++ compiler (GCC/g ++ supporting C++17).

The Social Network structure has been primarily implemented by two key data structures - AVL Trees and Graphs. The underlying structure of the Network is encapsulated by the graph, and the underlying structure/posts of each user in the network are encapsulated by the AVL Trees, corresponding to each user

AVLTree Class:
- Node Structure:
    - time_t key: Stores the Timestamp corresponding to each post created by the user
    - string post: Stores the content of the post created by the respective user
    - Node* left, Node* right: The standard left and right child pointers present in a binary Tree
    - int height: Augmentation field in the standard AVL structure to accomodate easy balance factor calculations during rotation implementations

- Functions:
    | Name | Arguments | Description
    | :---: | :---: | :---: |
    |AVLTree|<string name>| Constructor for AVL Class
    |height|<Node* node>| returns the height of the passed node
    |leftRotate|<Node* node>| Performs left Rotation for height balancing
    |rightRotate|<Node* node>| Performs right rotation for height balancing
    |getBalance|<Node* node>| Returns the balance factor for a given node
    |insertNodeHelper|<Node* root> <time_t key> <string post>| Helper function for node insertion - called by insert() function later as a public utility
    |deleteNodeHelper|<Node* root> <time_t key>| Helper function for node deletion, called by deleteNode() public utility later
    |minValueNode|<Node* node>| Returns the node with the minimum value in the subtree rooted at node
    |getRoot| -| Getter method for the root of the tree
    |setRoot|<Node* newRoot>| Setter method for the root of the tree
    |Inorder|<vector<string> ans> <root> | Returns the inorder traversal of the tree as the 'ans' vector

GRAPH Class
- Structure:
    - vector<AVLTree*> vertices: Stores all the vertcies of teh graph, which are basically the root nodes of the AVL trees corresponding to the concerned user
    - vector<pair<AVLTree*, AVLTree*>> edges:   Stores the edges of the graph - similar to the vertices vector
    - unordered_map<AVLTree*, vector<AVLTree*>> adjacency: The adjacency list representation of the graph

- Functions:
    - For complexity Analysis:
        - V: The number of vertices
        - E: The number of edges
        - v: The target user
        - deg(u): The degree of a node u in the graph
        - degm(v): The max degree of any friend of v
    |Name|Arguments|Description|Time Complexity|
    |:---:|:---:|:---:|:---:|
    |addUserHelper|string name|Adds a user to the network, ensuring the username is unique (case-insensitive check).|O(V)|
    |addFriendHelper|string name1, string name2|Establishes a mutual, undirected friendship between two existing users.|O(deg(v))
    |listNeighboursHelper|string name|Retrieves all direct friends of a given user, returned in sorted alphabetical order.|O(deg(v)log(deg(v)))|
    |degreeOfSeparation|string user1, string user2|Calculates the shortest path distance (friendship degree) between two users using BFS.|O(V + E)|
    |suggestFriendsHelper|string name, int N|Suggests up to N non-friends who share the highest number of mutual friends.|O(deg(v)degm(v))|
    |ShortestPath|	AVLTree* user1, AVLTree* user2|	Internal Breadth-First Search (BFS) utility to find the distance between two nodes.|O(V + E)|

- UTILITY/HELPER Functions:
    - N: Number of posts in the user's AVL Tree.
    - Nt: Total number of posts in the user's AVL Tree.
    - deg(A): Degree (number of friends) of user A (size of vector a).
    - deg(B): Degree (number of friends) of user B (size of vector b).
    |Name|Arguments|Description|Time Complexity|
    |:---:|:---:|:---:|:---:|
    |addPostHelper|<string name>, <string post>|Adds the given string post as a new node with appropriate time stamping to the AVL Tree corresponding to the concerned user, if the username already exists. Reports error message otherwise|O(logN)|
    |outputPostHelper|<string name> int<N>|Finds the user, performs an in-order traversal of all Nt posts, reverses the list, and returns the top N posts.|O(log(Nt))|
    |countCommons|<vector<AVLTree*> a>, <vector<AVLTree*> b>|Counts the number of common user nodes between two unsorted vectors of friends|O(deg(A)deg(B))|
    |comparator|vector<pair<AVLTree*, int> a>, <vector<AVLTree*, int> b>|Custom comparator used with the sort function to sort in the descending order of mutual friends, and then use the alphabetical nature of the names as a tie breaker|O(1)|

- GLOBAL VARIABLES:
    - unordered_map<AVLTree*, string> names: Maps the nodes of the graph to the user names of the corresponding users
    - unordered_map<string, AVLTree*> Nodes: Maps the usernames to the root nodes of the corresponding AVL Tree associated with the user.



## Installation And Setup
- Prerequisites
    - C++ Compiler: A compiler supporting the C++17 standard (e.g., GCC/G++ or Clang) is required.

    - Windows Users: This is typically provided via MinGW, Cygwin, or Visual Studio Build Tools.

- Build Instructions
    - g++ -std=c++17 -o socialnet LONG_ASSIGNMENT_MAJOR.cpp
This command compiles main.cpp and creates an executable file named socialnet

- Execution:
    - For Linux/macOS terminal, the execution command is:
        ./socialnet
    - For Windows(PowerShell/Command Prompt), the execution commmnd is: socialnet.exe or socialnet

## Demo Test Cases
For debugging purposes, we had used the following test cases, so as to get an understanding of the edge cases and handle error cases: (For all ADD_USER commands where valid addition is possible, we get a success message)
    |Command|Expected output|
    |:---:|:---:|
    |ADD_USER alice| Success Message
    |ADD_USER| bob
    |ADD_USER| charlie
    |ADD_USER| david
    |ADD_USER| eve
    |ADD_USER| Alice
    |ADD_FRIEND alice bob| "alice and bob are now friends"
    |ADD_FRIEND bob charlie| "bob and charlie are now friends"
    |ADD_FRIEND alice bob| "The two users already have a friend connection"
    |LIST_FRIENDS david| "david has no friends."
    |LIST_FRIENDS bob|  "The two users already have a friend connection"
    |ADD_USER frank| Success message
    |ADD_FRIEND charlie david  
    |ADD_FRIEND david eve
    |DEGREE_OF_SEPARATION bob bob	0
    |DEGREE_OF_SEPARATION alice bob	1
    |DEGREE_OF_SEPARATION alice eve	4
    |DEGREE_OF_SEPARATION alice frank Path... not found (or -1 if printing the  return value)
    |DEGREE_OF_SEPARATION alice "Error - One or both users do not exist."
    |ADD_FRIEND alice david	Alice is now friends with Bob and David.	Create Mutuals
	|SUGGEST_FRIENDS alice 1	Suggested friends for alice: charlie (Mutuals: Bob, David).	Simple Suggestion
    |ADD_USER george
    |ADD_USER hannah
    |ADD_FRIEND charlie george
    |ADD_FRIEND david george
    |ADD_FRIEND charlie hannah
    |ADD_FRIEND david hannah
    |SUGGEST_FRIENDS charlie 3	Suggested friends for charlie:alice (2 mutuals),george (0 mutuals),hannah (0 |mutuals)
    |SUGGEST_FRIENDS bob 0	"No friends suggested for bob
    |ADD_POST alice "first"
    |ADD_POST alice "second"
    |ADD_POST alice "third"
    |OUTPUT_POST alice 1	"third" (Newest post).
    |OUTPUT_POST alice -1 "third", "second", "first"
    |OUTPUT_POST alice 5	 Only the 3 existing posts are returned (third, second, first)
    |ADD_POST gina "fail" "Error: User does not exist."
    |OUTPUT_POST frank 5	"The user has no posts or does not exist."
    |QUIT	"Exititng the Social Network - see you soon !!"
## Authors

- Prasanna Prasad Mahajan
- Entry No. - 2024EE10805
- Department Of Electrical Engineering
- Indian Institute of Technology, Delhi

