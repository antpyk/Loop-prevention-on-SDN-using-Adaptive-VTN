# Loop-prevention-on-SDN-using-Adaptive-VTN
Software-Defined Networking (SDN) Research Project

# About this research and publication
In association with Thammasat University and CS LoxInfo Plc..

# Abstact
Loop is a most common problem in general and enterprise network. 
Spanning tree protocol (STP) is a standard loop detection and recovery by drop some network links to remove loop. 
All network switches require pre-configuration manually. Software-Defined Networking (SDN) has solved this problem. 
With SDN, the control plane is removed from network device's hardware and implements it in software call SDN controller instead. 
With the OpenFlow protocol, SDN controller centrally controls routing, network operation and each network device can be configuration centrally. 

This paper, we develop our loop prevention system based on VTN application. 
We provide automate loop prevention and routing management by calculate the best path by using Dijkstra's Algorithm. 
The packages flow generates by SDN and VTN application automatically.

# Experiment and Evaluation
The program leveraging the Northbound REST API to transfer data to OpenDaylight controller 
and using VTN application in JSON format using the standard HTTP methods. 
The HTTP methods provide the operations, such as create, read, update, and delete that can perform on the controller. 
Then we a develop routing management system by calculate the best path by using Dijkstra's Algorithm. 
To calculating cost for best path, the program generates the end to end flows based on 
combination of two performance metrics: the average path latency and the port bandwidth of an OpenFlow switch. 
When the topology changes, VTN generates flow entries automatically and then generate new flow entries by calculate the best path again. 
Users cannot configure a flow by themselves, the program generated flow entries automatically
