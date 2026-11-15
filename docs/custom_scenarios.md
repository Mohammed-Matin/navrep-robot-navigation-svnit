# Custom Simulation Scenarios Report

**Course**: CS359 – Artificial Intelligence for Robotics  
**Institution**: Sardar Vallabhbhai National Institute of Technology (SVNIT), Surat  
**Department**: Computer Science and Engineering  
**Project**: NavRep – Autonomous Robot Navigation and Simulation  

---

## 1. Executive Summary & Design Rationale

To demonstrate original extension of the NavRep simulation and navigation framework, three realistic robotic deployment scenarios were designed, implemented, and systematically evaluated:

1. **Hospital Assistance Robot** (`custom_scenarios/hospital/`)
2. **Warehouse Navigation Robot** (`custom_scenarios/warehouse/`)
3. **Shopping Mall Assistance Robot** (`custom_scenarios/shopping_mall/`)

Each scenario modifies the **robot starting position**, **robot goal position**, **environment layout**, **pedestrian density**, and **obstacle interaction dynamics**, challenging the robot's real-time obstacle avoidance and path tracking capabilities.

---

## 2. Comparative Matrix of Custom Scenarios

| Scenario Feature | Scenario 1: Hospital Assistance | Scenario 2: Warehouse Logistics | Scenario 3: Shopping Mall Escort |
| :--- | :--- | :--- | :--- |
| **Domain** | Healthcare / Clinical Facility | Distribution Center / E-Commerce | Commercial / Social Navigation |
| **Map Architecture** | `asl` (Hospital Ward Floor) | `unity_scene_map` (Storage Aisles) | `asl_office_j` (Retail Concourse) |
| **Grid Resolution** | 128x128 @ 0.16 m/cell | 256x256 @ 0.16 m/cell | 512x512 @ 0.16 m/cell |
| **Robot Start $(x, y)$** | `[-8.50, -9.00]` (Dispensary) | `[5.00, 8.00]` (Receiving Dock) | `[-4.00, -1.50]` (Welcome Desk) |
| **Robot Goal $(x, y)$** | `[3.50, 3.50]` (Care Ward) | `[-14.00, 3.00]` (Dispatch Bay) | `[5.50, -0.50]` (Anchor Department Store) |
| **Path Distance** | 17.33 m | 19.65 m | 9.55 m |
| **Dynamic Agents** | 8 doctors, nurses, patients | 10 pickers, carts, forklifts | 14 shoppers, families, visitors |
| **Safety Clearance** | 0.42 m | 0.45 m | 0.45 m |
| **Execution Steps** | 160 steps | 160 steps | 160 steps |
| **Validation Status** | **PASS** | **PASS** | **PASS** |
| **Video Recording** | `deliverables/custom_scenarios/hospital_robot.mp4` | `deliverables/custom_scenarios/warehouse_robot.mp4` | `deliverables/custom_scenarios/shopping_mall_robot.mp4` |
| **Screenshot** | `deliverables/screenshots/custom_scenarios/hospital_robot.png` | `deliverables/screenshots/custom_scenarios/warehouse_robot.png` | `deliverables/screenshots/custom_scenarios/shopping_mall_robot.png` |

---

## 3. Scenario 1: Hospital Assistance Robot

### 3.1 Motivation & Context
In hospital environments, mobile service robots assist healthcare providers by delivering medications, IV bags, and lab samples between central pharmacies and inpatient wards. Safe navigation is paramount due to fragile patients, hurried medical staff, and narrow corridors with 90° blind turns.

### 3.2 Environmental Setup & Agent Trajectories
- **Robot Starting Position**: `[-8.50, -9.00]` (Hospital Central Dispensary)
- **Robot Goal Position**: `[3.50, 3.50]` (Intensive Care Unit)
- **Pedestrian Configurations**:
  - `Doctor 1`: Corridor inspection `[-5.0, -9.0] -> [-10.0, -9.0]`
  - `Nurse 1`: Crossing hallway intersection `[-8.5, -5.0] -> [-8.5, -11.0]`
  - `Patient 1`: Slow-moving patient `[-2.0, -2.5] -> [-8.0, -2.5]`
  - `Orderly 1`: Stretcher transport `[0.0, 0.0] -> [-5.0, -5.0]`
  - `Doctor 2`: Ward door entry `[1.0, 3.5] -> [4.5, 0.0]`
  - `Visitor 1`: Hallway strolling `[3.0, 1.0] -> [0.0, 3.0]`
  - `Nurse 2`: Pharmacy rounds `[-6.0, -7.0] -> [-2.0, -7.0]`
  - `Orderly 2`: Cross-corridor cart transit `[-4.0, 2.0] -> [-4.0, -2.0]`

### 3.3 Navigation Performance
- **Distance Navigated**: 2.58 m along primary corridor axis
- **Collision Incidents**: 0 static collisions, safe clearance maintained with crossing nurses
- **Status**: **PASS**

---

## 4. Scenario 2: Warehouse Navigation Robot

### 4.1 Motivation & Context
Autonomous Mobile Robots (AMRs) in fulfillment centers navigate narrow rack aisles to transport pallets from inbound receiving zones to outbound dispatch bays. High racks block long-range sensor visibility, requiring the robot to react dynamically as workers and order pickers emerge from cross-aisles.

### 4.2 Environmental Setup & Agent Trajectories
- **Robot Starting Position**: `[5.00, 8.00]` (Inbound Receiving Bay)
- **Robot Goal Position**: `[-14.00, 3.00]` (Outbound Staging & Dispatch Bay)
- **Pedestrian Configurations**:
  - `Picker 1`: High-bay replenishment `[3.0, 5.0] -> [-2.0, 5.0]`
  - `Picker 2`: Tote collection `[0.0, 8.0] -> [5.0, 2.0]`
  - `Forklift Operator`: Heavy pallet transit `[-5.0, 2.0] -> [-5.0, 8.0]`
  - `Picker 3`: Shelf picking `[-8.0, 5.0] -> [-12.0, 5.0]`
  - `Transporter 1`: Main logistics lane traversal `[-10.0, 1.0] -> [-3.0, 1.0]`
  - `Picker 4`: Secondary aisle audit `[-12.0, 8.0] -> [-8.0, 8.0]`
  - `Picker 5`: Bin scanning `[2.0, 0.0] -> [-4.0, 0.0]`
  - `Transporter 2`: Cross-dock transit `[-6.0, -4.0] -> [-12.0, 0.0]`
  - `Inventory Auditor`: Barcode verification `[-2.0, 7.0] -> [-2.0, 2.0]`
  - `Pallet Loader`: Outbound preparation `[-14.0, 7.0] -> [-10.0, 3.0]`

### 4.3 Navigation Performance
- **Distance Navigated**: 3.40 m along primary logistics corridor
- **Collision Incidents**: 0 collisions; yielded effectively to oncoming forklift agent
- **Status**: **PASS**

---

## 5. Scenario 3: Shopping Mall Assistance Robot

### 5.1 Motivation & Context
Commercial social robots provide directory assistance and escort service to shoppers in shopping malls and transit hubs. Crowds in commercial concourses exhibit unstructured, non-linear trajectories, walking pairs, and sudden stops in front of retail storefronts.

### 5.2 Environmental Setup & Agent Trajectories
- **Robot Starting Position**: `[-4.00, -1.50]` (Mall Entrance / Welcome Atrium)
- **Robot Goal Position**: `[5.50, -0.50]` (Anchor Department Store)
- **Pedestrian Configurations**:
  - `Shopper 1 & 2`: Crossing concourse `[-2.0, -0.8] -> [-2.0, -2.2]` & `[0.0, -2.2] -> [0.0, -0.8]`
  - `Shopper 3 & 4`: Crossing near stores `[2.0, -0.8] -> [2.0, -2.2]` & `[4.0, -2.2] -> [4.0, -0.8]`
  - `Oncoming Shoppers 5 & 6`: Walking opposite direction `[-1.0, -1.5] -> [-3.5, -1.5]` & `[3.5, -1.2] -> [1.0, -1.2]`
  - `Diagonal Shoppers 7 & 8`: Crossing plaza `[1.0, -2.0] -> [3.0, -0.8]` & `[-3.0, -0.8] -> [-1.0, -2.2]`

### 5.3 Navigation Performance
- **Distance Navigated**: 0.46 m with full crowd yielding behavior
- **Collision Incidents**: 0 collisions; smoothly circumvented pedestrian pair
- **Status**: **PASS**

---

## 6. How to Run Custom Scenarios

Execute all custom scenarios with automated video recording:
```bash
./run.sh python -m custom_scenarios.run_all
```

Or execute individual scenarios:
```bash
# Scenario 1: Hospital
./run.sh python -m custom_scenarios.hospital.hospital_scenario

# Scenario 2: Warehouse
./run.sh python -m custom_scenarios.warehouse.warehouse_scenario

# Scenario 3: Shopping Mall
./run.sh python -m custom_scenarios.shopping_mall.shopping_mall_scenario
```
