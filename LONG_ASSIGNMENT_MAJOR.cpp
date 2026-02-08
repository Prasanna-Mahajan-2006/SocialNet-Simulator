#include<iostream>
#include<vector>
#include<queue>
#include<map>
#include<unordered_map>
#include<stack>
#include<ctime>
#include<algorithm>

using namespace std;

// Initial declaration for AVLTree and some helper/utility functions
class AVLTree;
string upperToLower(string s);
static bool comparator(pair<AVLTree*, int> a, pair<AVLTree*, int> b);

unordered_map<AVLTree*, string> names;
unordered_map<string, AVLTree*> Nodes;

string upperToLower(string s){
    string word = "";
    int m = s.size();
    for(int i = 0; i < m; i ++){
        if(s[i] >= 'A' && s[i] <= 'Z'){
            word += s[i] - 'A' + 'a';
        }
        else
            word += s[i];
    }
    return word;
}

static bool comparator(pair<AVLTree*, int> a, pair<AVLTree*, int> b){
    if(a.second != b.second){
        return a.second > b.second;
    }
    else{
        return names[a.first] < names[b.first];
    }
}

int countCommons(vector<AVLTree*> a, vector<AVLTree*> b){
    int count = 0;
    int m = a.size();
    for(int i = 0; i < m; i ++){
        if(find(b.begin(), b.end(), a[i]) != b.end())
            count ++;
    }
    return count;
}

struct Node {
    time_t key;
    Node* left;
    Node* right;
    int height;
    string post;
    Node(time_t k, string p) : key(k), left(nullptr), right(nullptr), height(0), post(p) {}
};

class AVLTree {
private:
    Node* root;
    int height(Node* N) {
        if (N == nullptr)
            return -1;
        return N->height;
    }

    Node* rightRotate(Node* y) {
        Node* x = y->left;
        Node* T2 = x->right;
        x->right = y;
        y->left = T2;
        y->height = max(height(y->left), height(y->right)) + 1;
        x->height = max(height(x->left), height(x->right)) + 1;
        return x;
    }

    Node* leftRotate(Node* x) {
        Node* y = x->right;
        Node* T2 = y->left;
        y->left = x;
        x->right = T2;
        x->height = max(height(x->left), height(x->right)) + 1;
        y->height = max(height(y->left), height(y->right)) + 1;
        return y;
    }

    int getBalance(Node* N) {
        if(N == NULL){
            return 0;
        }
        return height(N -> left) - height(N -> right);
    }
    Node* minValueNode(Node* node) {
        Node* current = node;
        while (current->left != nullptr)
            current = current->left;
        return current;
    }

    void deleteTree(Node* node) {
        if (node != nullptr) {
            deleteTree(node->left);
            deleteTree(node->right);
            delete node;
        }
    }
public:
    Node* insertHelper(Node* node, time_t key, string p) {
        if (node == nullptr)
            return new Node(key, p);

        if (key < node->key)
            node->left = insertHelper(node->left, key, p);
        else if (key > node->key)
            node->right = insertHelper(node->right, key, p);
        else
            return node;

        node->height = 1 + max(height(node->left), height(node->right));
        int balance = getBalance(node);

        if (balance > 1 && key < node->left->key)
            return rightRotate(node);

        if(balance < -1 && key > node -> right -> key)
            return leftRotate(node);
        
        if(balance > 1 && key > node -> left -> key){
            node -> left = leftRotate(node -> left);
            return rightRotate(node);
        }

        if(balance < -1 && key < node -> right -> key){
            node -> right = rightRotate(node -> right);
            return leftRotate(node);
        }

        return node;
    }
    
    Node* deleteNodeHelper(Node* root, time_t key) {
        if (root == nullptr) return root;

        if (key < root->key)
            root->left = deleteNodeHelper(root->left, key);
        else if (key > root->key)
            root->right = deleteNodeHelper(root->right, key);
        else {
            if ((root->left == nullptr) || (root->right == nullptr)) {
                Node* temp = root->left ? root->left : root->right;
                if (temp == nullptr) {
                    temp = root;
                    root = nullptr;
                } else
                    *root = *temp;
                delete temp;
            } else {
                Node* temp = minValueNode(root->right);
                root->key = temp->key;
                root->right = deleteNodeHelper(root->right, temp->key);
            }
        }

        if (root == nullptr) return root;

        root->height = 1 + max(height(root->left), height(root->right));
        int balance = getBalance(root);

        if (balance > 1 && getBalance(root->left) >= 0)
            return rightRotate(root);

        if (balance > 1 && getBalance(root->left) < 0) {
            root->left = leftRotate(root->left);
            return rightRotate(root);
        }

        if (balance < -1 && getBalance(root->right) <= 0)
            return leftRotate(root);

        if (balance < -1 && getBalance(root->right) > 0) {
            root->right = rightRotate(root->right);
            return leftRotate(root);
        }

        return root;
    }

    AVLTree(string username) {
        root = nullptr;
        names[this] = username;
    }

    ~AVLTree() {
        deleteTree(root);
    }

    void insert(int key, string post) {
        root = insertHelper(root, key, post);
    }

    void deleteNode(int key) {
        root = deleteNodeHelper(root, key);
    }

    int getRootKey() {
        if(root == NULL)
            return -1;
        return root -> key;
    }

    Node* getRoot(){
        return root;
    }

    void setRoot(Node* newRoot) {
        root = newRoot;
    }
    
    void Inorder(vector<string>& ans, Node* root){
        if(root == NULL)
            return;
        Inorder(ans,root -> left);
        ans.push_back(root -> post);
        Inorder(ans, root -> right);
    }
};

class Graph{
    private:
        vector<AVLTree*> vertices;
        vector<pair<AVLTree*, AVLTree*>> edges;
        unordered_map<AVLTree*, vector<AVLTree*>> adjacency;
    public:
        void addUserHelper(string name){
            string lower_name = upperToLower(name);
            int m = vertices.size();
            for(int i = 0; i < m; i ++){
                if(names[vertices[i]] == lower_name){
                    cout << "This username has been taken! Please enter another name" << endl;
                    return;
                }
            }
            cout << "Welcome to the SocialNet, " << name << endl;
            AVLTree* newUser = new AVLTree(lower_name);
            vertices.push_back(newUser);
            names[newUser] = lower_name;
            Nodes[lower_name] = newUser;
        }
        
        void addFriendHelper(string name1, string name2){
            string n1 = upperToLower(name1), n2 = upperToLower(name2);
            
            if(Nodes.count(n1) == 0 || Nodes.count(n2) == 0){
                cout << "The user(s) do not exist in the network!" << endl;
                return;
            }
            AVLTree* u1 = Nodes[n1];
            AVLTree* u2 = Nodes[n2];
            for(AVLTree* nbr : adjacency[u1]){
                if(nbr == u2){
                    cout << "The two users already have friend connection !!" << endl;
                    return;
                }
            }
            pair<AVLTree*, AVLTree*> p = make_pair(u1, u2);
            edges.push_back(p);
            adjacency[u1].push_back(u2);
            adjacency[u2].push_back(u1);
            cout << name1 << " and " << name2 << " are now friends." << endl;
        }

        vector<string> listNeighboursHelper(string name){
            vector<string> ans;
            string n1 = upperToLower(name);
            
            if(Nodes.count(n1) == 0){
                cout << "User " << name << " not found." << endl;
                return ans;
            }
            AVLTree* userNode = Nodes[n1];
            for(AVLTree* n: adjacency[userNode]){
                ans.push_back(names[n]);
            }
            sort(ans.begin(), ans.end());
            return ans;
        }
        
        vector<string> suggestFriendsHelper(string name, int N){
            string n = upperToLower(name);
            vector<string> ans;
            
            if(Nodes.count(n) == 0){
                cout << "Error - No such username exists" << endl;
                return ans;
            }

            if(N <= 0)
                return ans;
            
            AVLTree* node = Nodes[n];
            vector<pair<AVLTree*, int>> allSeconds;
            
            vector<AVLTree*> v = adjacency[node];
            unordered_map<AVLTree*, bool> firstNbr;
            unordered_map<AVLTree*, int> mutualCounts;
            
            firstNbr[node] = true;
            for(AVLTree* friendNode : v){
                firstNbr[friendNode] = true;
            }
            
            for(AVLTree* friendNode : v){
                vector<AVLTree*> u = adjacency[friendNode];
                for(AVLTree* potentialFriend : u){
                    
                    if(firstNbr.count(potentialFriend)){
                        continue;
                    }
                    else{
                        mutualCounts[potentialFriend] ++;
                    }
                }
            }
            
            for(auto i: mutualCounts){
                pair<AVLTree*, int> p = make_pair(i.first, i.second);
                allSeconds.push_back(p);
            }
            sort(allSeconds.begin(), allSeconds.end(), comparator);
            int suggestions_to_take = min((int)allSeconds.size(), N); 
            for(int i = 0; i < suggestions_to_take; i ++){
                ans.push_back(names[allSeconds[i].first]);
            }
            
            return ans;
        }

        int ShortestPath(AVLTree* user1, AVLTree* user2){
            if(user1 == user2)
                return 0;
            unordered_map<AVLTree*, int> distance;
            queue<AVLTree*> q;
            
            if(!user1 || !user2) return -1;

            distance[user1] = 0;
            q.push(user1);

            while(!q.empty()){
                AVLTree* node = q.front();
                q.pop();

                for(AVLTree* nbr: adjacency[node]){
                    if(distance.count(nbr) == 0){ 
                        distance[nbr] = distance[node] + 1;
                        if(nbr == user2)
                            return distance[nbr];
                        q.push(nbr);
                    }
                }
            }
            return -1;
        }

        int degreeOfSeparation(string user1, string user2){
            string n1 = upperToLower(user1), n2 = upperToLower(user2);
            
            if(n1 == n2)
                return 0;

            if(Nodes.count(n1) == 0 || Nodes.count(n2) == 0){
                cout << "Error - One or both users do not exist." << endl;
                return -1; 
            }
            
            AVLTree* node1 = Nodes[n1];
            AVLTree* node2 = Nodes[n2];
            
            return ShortestPath(node1, node2);
        }
};

void addPostHelper(string username, string post){
    // Resolved error: n is defined immediately
    string n = upperToLower(username); 
    
    if(Nodes.count(n) == 0){
        cout << "Error: User does not exist." << endl;
        return;
    }
    AVLTree* update_user = Nodes[n];
    
    // Resolved error: Use the public setter instead of accessing private root member directly
    Node* newRoot = update_user -> insertHelper(update_user->getRoot(), time(NULL), post);
    update_user->setRoot(newRoot); 

    cout << "The post has been added successfully" << endl;
}

vector<string> outputPostHelper(string name, int N){
    string n = upperToLower(name);
    vector<string> allPosts;
    
    if(Nodes.count(n) == 0){
        cout << "Error: User does not exist." << endl;
        return allPosts;
    }
    AVLTree* node = Nodes[n];
    Node* start = node -> getRoot();

    node ->Inorder(allPosts, start);

    if(allPosts.empty()){
        return allPosts;
    }
    reverse(allPosts.begin(), allPosts.end());
    if(N == -1){
        return allPosts;
    }
    int num_to_return = min((int)allPosts.size(), N);
    vector<string> ans(allPosts.begin(), allPosts.begin() + num_to_return);

    return ans;
}


int main(){
    Graph SocialNet;
    string command;
    
    cout << "Enter the commands - enter QUIT to exit..." << endl;
    while(cin >> command){

        if(command == "ADD_USER"){
            string name;
            cin >> name;
            SocialNet.addUserHelper(name);
        }
        else if(command == "ADD_FRIEND"){
            string name1, name2;
            cin >> name1 >> name2;
            SocialNet.addFriendHelper(name1, name2);
        }
        else if(command == "LIST_FRIENDS"){
            string name;
            cin >> name;
            vector<string> res = SocialNet.listNeighboursHelper(name);
            if(res.size() > 0){
                cout << "Friends of " << name << " are:" << endl;
                for(string friend_name : res){
                    cout << friend_name << endl;
                }
            } else {
                cout << name << " has no friends." << endl;
            }
        }
        else if(command == "SUGGEST_FRIENDS"){
            string name;
            int n;
            cin >> name >> n;
            vector<string> res = SocialNet.suggestFriendsHelper(name, n);
            if(res.size() > 0){
                cout << "Suggested friends for " << name << ":" << endl;
                for(string suggest_name : res){
                    cout << suggest_name << endl;
                }
            } else {
                cout << "No friends suggested for " << name << "." << endl;
            }
        }
        else if(command == "DEGREE_OF_SEPARATION"){
            string name1 , name2;
            cin >> name1 >> name2;
            int degree = SocialNet.degreeOfSeparation(name1, name2);
            if(degree != -1){
                cout << "Degree of separation between " << name1 << " and " << name2 << " is: " << degree << endl;
            } else {
                cout << "Path between " << name1 << " and " << name2 << " not found." << endl;
            }
        }
        else if(command == "ADD_POST"){
            string name, post;
            cin >> name >> post;
            addPostHelper(name, post);
        }
        else if(command == "OUTPUT_POST"){
            string name;
            int n;
            cin >> name >> n;
            vector<string> res = outputPostHelper(name, n);
            if(res.empty()){
                cout << "The user has no posts or does not exist." << endl;
                continue; 
            }
            cout << "Printing posts (Newest first)" << endl;
            int m = res.size();
            for(int i = 0; i < m; i ++){
                cout << res[i] << endl;
            } 
            cout << "End of posts" << endl;
        }
        else if(command == "QUIT"){
            cout << "Exititng the Social Network - see you soon !!" << endl;
            break;
        }
        else{
            cout << "INVALID COMMNAND - ABORTING !!" << endl;
        }
    }
}