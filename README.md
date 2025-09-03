# multicloud-sdn-lab-

Python SDN Controller

A Python-based Software-Defined Networking (SDN) controller built using Ryu and OpenFlow, designed for network automation, simulation, and hands-on learning. This project allows you to programmatically control network traffic, simulate networks locally using Mininet, and provides a foundation for future multicloud networking experiments.

⸻

Overview

This project was created to explore SDN concepts in a practical, hands-on way. By using Python and Ryu, you can dynamically manage traffic, implement flow rules, and monitor networks—all without requiring physical network hardware.

Key goals:
	•	Forward and manage network traffic programmatically
	•	Simulate networks with Mininet
	•	Experiment with flow rules, routing, and policies
	•	Lay the groundwork for multicloud SDN experiments

⸻

Features
	•	Python-based controller using Ryu
	•	OpenFlow-compatible for virtual or real switches
	•	Local network simulation using Mininet
	•	Extensible for custom rules, monitoring, or multicloud integration
	•	Clear, modular code for learning and expansion

⸻

Project Structure
python-sdn-controller/
├── controllers/
│   └── simple_controller.py       # Main SDN controller
├── mininet-scripts/
│   └── single_switch_topo.py      # Custom Mininet topology script
├── requirements.txt               # Python dependencies
├── README.md
└── LICENSE

Getting Started

1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/python-sdn-controller.git
cd python-sdn-controller

2. Install Dependencies
pip install -r requirements.txt
sudo apt-get install mininet

Mininet is required for simulating the network. This is typically installed on Linux or WSL for Windows.

3. Run a Default Mininet Network
sudo mn --topo single,3 --controller remote

This creates:
	•	1 virtual switch
	•	3 virtual hosts
	•	All traffic controlled by your SDN controller

⸻

4. Run the Custom Topology Script
sudo python mininet-scripts/single_switch_topo.py

This script creates the same network but allows you to easily modify hosts, switches, or links programmatically. It connects automatically to your Ryu controller at 127.0.0.1.


⸻

5. Start the SDN Controller
ryu-manager controllers/simple_controller.py

Your controller will now:
	•	Forward packets to the correct hosts
	•	Monitor network events
	•	Be ready for extensions like traffic blocking, prioritization, or routing between cloud networks

How It Works

The controller listens for switch events and installs flow rules dynamically. In this version, it acts as a basic learning switch, but it can be extended to:
	•	Block or prioritize specific traffic
	•	Implement Quality of Service (QoS) rules
	•	Collect and monitor network traffic statistics
	•	Integrate with multiple cloud providers (AWS, Azure, GCP) for centralized SDN control

⸻

Next Steps / Ideas
	•	Dynamic routing between multiple network segments
	•	Traffic prioritization and QoS
	•	Integrate with cloud VPCs for multicloud SDN experiments
	•	Add security rules and automated network policies
	•	Logging and analytics of traffic flows

⸻

Requirements
	•	Python 3.8+
	•	Ryu SDN framework
	•	Mininet for network simulation
	•	Linux environment or WSL for Windows (recommended)

⸻

License

This project is open source under the MIT License. See LICENSE for details.

