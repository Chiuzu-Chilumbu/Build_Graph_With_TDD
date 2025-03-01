# **Graph Data Structure with TDD, BDD, UI Testing, and CI/CD Visualization**

## **📌 Project Overview**  

This project is a **comprehensive exploration of Test-Driven Development (TDD), Behavior-Driven Development (BDD), and UI automation testing** while implementing a **Graph Data Structure with Stack and Queue support**.  

It builds on foundational projects for [Queue](https://github.com/Chiuzu-Chilumbu/Build_Queue_With_TDD) and [Stack](https://github.com/Chiuzu-Chilumbu/Build_Stack_With_TDD), culminating in a **full-stack graph visualization system** with **Selenium UI tests** and **automated deployment using GitHub Actions and Heroku**.

### **🚀 Key Features**  
✅ **Graph, Stack & Queue Implementation** – Developed using TDD with unit tests for core operations.  
✅ **Graph Traversal (BFS & DFS)** – Implemented using **Stacks (DFS) and Queues (BFS)**.  
✅ **Selenium-Based UI Testing** – **Page Object Model (POM)** ensures **maintainable** and **scalable UI automation**.  
✅ **BDD with pytest-bdd** – Feature files describe graph behaviors (e.g., pathfinding, cycle detection).  
✅ **Graph Visualization** – Displays **graph structure and traversal algorithms in real-time**.  
✅ **CI/CD Integration** – Automated **testing, deployment to Heroku, and visualization updates**.  

---

## **🛠 Development Approach**

### **1️⃣ Test-Driven Development (TDD)**
TDD is used to **incrementally build and refine** Graph, Stack, and Queue operations:  
🔹 **Graph Operations** – Nodes, edges, directed & undirected graphs, weighted graphs.  
🔹 **Stack & Queue Support** – Used for **Graph Traversals (BFS & DFS)**.  
🔹 **Unit Testing with pytest** – Ensures correctness of all graph operations.  

### **2️⃣ Behavior-Driven Development (BDD)**
BDD makes **Graph behavior readable** for both developers and stakeholders:  
✔ **Feature Files** – Written using **Gherkin syntax** (`.feature` files).  
✔ **pytest-bdd Step Definitions** – Automates user scenarios (e.g., **finding shortest paths, detecting cycles**).  

### **3️⃣ UI Testing with Selenium**
To verify **Graph, Stack, and Queue UI**, we implemented:  
✔ **Page Object Model (POM)** – Keeps test logic structured and **reusable**.  
✔ **Selenium Tests** – Automates **push/pop (Stack), enqueue/dequeue (Queue), and Graph UI interactions**.  
✔ **Handling Stale Elements** – Explicit waits (`WebDriverWait`) prevent flaky tests.  

### **4️⃣ Continuous Integration & Deployment (CI/CD)**
💡 **GitHub Actions Pipeline** automates:  
✅ **Unit & BDD Tests** – Run on every commit.  
✅ **Selenium UI Tests** – Currently **excluded due to headless browser limitations**.  
✅ **Deployment** – Automatically **deploys Graph visualization to Heroku**.  

---

## **🎯 Real-World Applications**
Graphs power **critical applications** in various domains:  
🔹 **Networking** – Routing algorithms (e.g., **Dijkstra’s shortest path**).  
🔹 **Social Media** – Friend recommendations via **Graph Traversal**.  
🔹 **Web Crawling** – DFS/BFS for indexing search engines.  
🔹 **AI & Robotics** – Pathfinding in **autonomous navigation**.  

---

## **🔗 Deployment**
The project is **deployed to Heroku**, where Graph visualizations are automatically updated.  

✅ **Live App URL:** [https://build-graph-with-tdd.herokuapp.com](https://build-graph-with-tdd.herokuapp.com)  

---

## **📜 Acknowledgments**
- Inspired by **data structure implementations in Python**.  
- Special thanks to the **testing and open-source communities**.  

---

🔥 **This project shows the importance of starting small and building more complex software using systematic testing, structured automation, and continuous deployment.** Let’s keep building! 🚀
