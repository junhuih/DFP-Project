# College Helper

## Group
Yifan Cheng - yifanc3@andrew.cmu.edu

Skylar Du - xiwend@andrew.cmu.edu

Yashash Gaurav - ygaurav@andrew.cmu.edu

Mark He - junhuih@andrew.cmu.edu


## 1. What does College Helper do? 

College Helper is mainly for high school students to get recommendations based on their preference and explore information on colleges and careers. 

Our goal is “To make application information both accessible and transparent to ALL students.”

Users can do 4 things in College Helper: 

1. See recommended colleges base on your preference
2. See top level stats about colleges
3. Browse careers
4. Search colleges

## 2. How to use it? 

### 2.1 Install Anaconda with Python 3.8
Download Link: https://www.anaconda.com/products/individual#Links

Then follow the instruction to install it. 

### 2.2 Build the environment

Follow the below instructions or you can just use our 'environment.yaml' to create your own environment

```
conda env create -f environment.yaml
```

else:

1. Open Anaconda Navigator
2. Click "Environments", then click "Channels"
![image](https://user-images.githubusercontent.com/90162689/137042205-d3319e26-85c9-4878-919f-ad6fba926c96.png)
3. Click "add" and type "conda-forge", then click "update channels"
![image](https://user-images.githubusercontent.com/90162689/137041805-7b21d522-ca59-44b6-85dd-25f5c7dfa7eb.png)
4. Create new environment named "college_helper", tick "Python 3.8"
![image](https://user-images.githubusercontent.com/90162689/137042002-2fc0cce5-4cab-4d5a-9db3-c2e81119f5d4.png)
5. Search for the following packages and install them
![image](https://user-images.githubusercontent.com/90162689/137042031-64e2f335-8d11-4d97-add3-ed95931b2e46.png)
![image](https://user-images.githubusercontent.com/90162689/137042041-fca62f07-e28c-4d09-b910-0af93f700feb.png)
![image](https://user-images.githubusercontent.com/90162689/137042049-f8d46812-445e-45fc-90ce-2f14f8c412bc.png)
![image](https://user-images.githubusercontent.com/90162689/137042054-dde7c886-7cba-4df2-9caa-6dcbdd0a020b.png)
![image](https://user-images.githubusercontent.com/90162689/137042067-f8eb5cae-e6fb-401f-b492-d874cde259d4.png)
![image](https://user-images.githubusercontent.com/90162689/137048200-76fb98a2-327c-4d74-8760-c01c56aa1fa8.png)
![image](https://user-images.githubusercontent.com/90162689/137048212-4db154e9-7af9-4eaa-988e-9bf28d73cdc5.png)


### 2.3 Run the college_helper.py
1. Install Spyder on the current environment.

2. Applications on "college_helper"
![image](https://user-images.githubusercontent.com/90162689/137043910-119e9cef-1939-40ad-904c-134eb2b942f6.png)

3. Launch Spyder to run the college_helper.py

### 2.4 Navigating the Application & Demo Video
Menu: 
1. See recommended colleges base on your preference
2. See top level stats about colleges
3. Browse careers
4. Search colleges
5. Refresh data - Only refreshes data that does not need a WebDriver. To collect all data, make sure you set the Edge Driver path in the fetch_all_data.py file and uncomment the code line in refresh_all_data() method.
6. Help! - Shows our dear client what our application will do for them

Demo video: https://www.youtube.com/watch?v=V7iRnBtlZ7c
