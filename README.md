# BTech-Projects
This repository contains the documentation of all the projects that i have undertaken as an undergrad at the Department of Electrical Engineering, Indian Institute of Technology, Delhi.

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

| Name | Arguments | Description |
| :--- | :--- | :--- |
| AVLTree | `<string name>` | Constructor for AVL Class |
| height | `<Node* node>` | returns the height of the passed node |
| leftRotate | `<Node* node>` | Performs left Rotation for height balancing |
| rightRotate | `<Node* node>` | Performs right rotation for height balancing |
| getBalance | `<Node* node>` | Returns the balance factor for a given node |
| insertNodeHelper| `<Node* root> <time_t key> <string post>` | Helper function for node insertion |
| deleteNodeHelper| `<Node* root> <time_t key>` | Helper function for node deletion |
| minValueNode | `<Node* node>` | Returns node with minimum value in subtree |
| getRoot | - | Getter method for the root of the tree |
| setRoot | `<Node* newRoot>` | Setter method for the root of the tree |
| Inorder | `<vector<string> ans> <root>` | Returns the inorder traversal as a vector |

GRAPH Class
- Structure:
    - vector<AVLTree*> vertices: Stores all the vertices of the graph
    - vector<pair<AVLTree*, AVLTree*>> edges: Stores the edges of the graph
    - unordered_map<AVLTree*, vector<AVLTree*>> adjacency: The adjacency list representation

- Functions:

| Name | Arguments | Description | Time Complexity |
| :--- | :--- | :--- | :--- |
| addUserHelper | string name | Adds a user to the network (unique check). | $O(V)$ |
| addFriendHelper | string n1, n2 | Establishes a mutual friendship. | $O(\text{deg}(v))$ |
| listNeighboursHelper | string name | Retrieves friends in sorted alphabetical order. | $O(\text{deg}(v) \log(\text{deg}(v)))$ |
| degreeOfSeparation | string u1, u2 | Shortest path distance using BFS. | $O(V + E)$ |
| suggestFriendsHelper | string name, int N | Suggests friends based on mutual connections. | $O(\text{deg}(v) \cdot \text{deg}_m(v))$ |
| ShortestPath | AVLTree* u1, u2 | Internal BFS utility to find distance. | $O(V + E)$ |

- UTILITY/HELPER Functions:

| Name | Arguments | Description | Time Complexity |
| :--- | :--- | :--- | :--- |
| **addPostHelper** | `<string name>, <string post>` | Adds post with timestamping to AVL Tree. | $O(\log N)$ |
| **outputPostHelper**| `<string name>, int N` | Returns top N posts via in-order traversal. | $O(\log N_t)$ |
| **countCommons** | `<vector> a, b` | Counts common nodes between friend vectors. | $O(\text{deg}(A) \cdot \text{deg}(B))$ |
| **comparator** | `pair a, b` | Sorts by mutual friends then alphabetical names. | $O(1)$ |

## Installation And Setup
- **Prerequisites**: C++ Compiler supporting C++17 (GCC/G++ or Clang).
- **Build**: `g++ -std=c++17 -o socialnet LONG_ASSIGNMENT_MAJOR.cpp`
- **Execution**: `./socialnet` (Linux/Mac) or `socialnet.exe` (Windows).

## Demo Test Cases

| Command | Expected Output |
| :--- | :--- |
| `ADD_USER alice` | Success Message |
| `ADD_FRIEND alice bob` | "alice and bob are now friends" |
| `DEGREE_OF_SEPARATION alice eve` | `4` |
| `OUTPUT_POST alice 1` | "third" (Newest post) |
| `QUIT` | "Exiting the Social Network - see you soon !!" |

## Authors
- **Prasanna Prasad Mahajan** (Entry No. 2024EE10805)
- Department Of Electrical Engineering, IIT Delhi